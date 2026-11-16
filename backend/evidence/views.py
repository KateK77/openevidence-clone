import re

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import IntegrityError, transaction, connection, DatabaseError
from django.http import Http404
from django.middleware.csrf import get_token
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.throttling import SimpleRateThrottle, UserRateThrottle

from . import exports, pubmed, rag, llm, serializers as s
from .models import Conversation, Evidence, Preferences, Publication, SavedPublication, SavedSearch, Turn


class AuthThrottle(SimpleRateThrottle):
    scope = 'auth'

    def get_cache_key(self, request, view):
        return self.cache_format % {'scope': self.scope, 'ident': self.get_ident(request)}


class ResearchThrottle(UserRateThrottle):
    scope = 'research'


class LiteratureThrottle(UserRateThrottle):
    scope = 'literature'


class ModelCheckThrottle(UserRateThrottle):
    scope = 'model_check'


def validated(serializer, data, **kwargs):
    form = serializer(data=data, **kwargs)
    form.is_valid(raise_exception=True)
    return form.validated_data


@extend_schema(responses=dict)
@api_view(['GET'])
@permission_classes([AllowAny])
def health(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT 1')
    except DatabaseError:
        return Response({'service': 'medevidence', 'status': 'unavailable'}, status=503)
    return Response({'service': 'medevidence', 'version': '3.0.0', 'status': 'ok', 'port': request.META.get('SERVER_PORT'),
                     'database': connection.vendor,
                     'generation_configured': llm.configuration()['configured']})


@extend_schema(responses=dict)
@ensure_csrf_cookie
@api_view(['GET'])
@permission_classes([AllowAny])
def session(request):
    return Response({'user': s.Profile(request.user).data if request.user.is_authenticated else None,
                     'public_demo': settings.PUBLIC_DEMO,
                     'csrf': get_token(request), 'model': settings.LLM_MODEL,
                     'generation_configured': llm.configuration()['configured'], 'synthesis': llm.capability()})


@extend_schema(request=None, responses=dict)
@api_view(['GET', 'POST'])
@throttle_classes([ModelCheckThrottle])
def synthesis_status(request):
    # The body is deliberately ignored: clients cannot choose a URL or send arbitrary prompts.
    return Response(llm.check_connection() if request.method == 'POST' else llm.capability())


@extend_schema(request=s.Credentials, responses={201: dict})
@api_view(['POST'])
@permission_classes([AllowAny])
@throttle_classes([AuthThrottle])
@csrf_protect
def register(request):
    data = validated(s.Credentials, request.data)
    user = User(username=data['username'])
    try:
        validate_password(data['password'], user)
    except DjangoValidationError as error:
        raise ValidationError({'password': list(error.messages)}) from None
    user.set_password(data['password'])
    try:
        with transaction.atomic():
            user.save(force_insert=True)
    except IntegrityError:
        raise ValidationError({'username': 'This username is unavailable.'}) from None
    login(request, user)
    return Response({'user': s.Profile(user).data, 'csrf': get_token(request)}, status=201)


@extend_schema(request=s.Credentials, responses=dict)
@api_view(['POST'])
@permission_classes([AllowAny])
@throttle_classes([AuthThrottle])
@csrf_protect
def sign_in(request):
    user = authenticate(request, **validated(s.Credentials, request.data))
    if user is None:
        return Response({'detail': 'Invalid username or password.'}, status=401)
    login(request, user)
    return Response({'user': s.Profile(user).data, 'csrf': get_token(request)})


@extend_schema(request=None, responses=dict)
@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_protect
def sign_out(request):
    logout(request)
    return Response({'user': None, 'csrf': get_token(request)})


@extend_schema(request=s.Profile, responses=s.Profile)
@api_view(['GET', 'PATCH'])
def profile(request):
    if (settings.PUBLIC_DEMO and request.user.username in settings.PUBLIC_DEMO_USERS
            and request.method == 'PATCH'):
        return Response({'detail': 'Shared demo profiles and credentials are protected. Create your own synthetic account to edit a profile.'}, status=403)
    serializer = s.Profile(request.user, data=request.data, partial=True)
    if request.method == 'PATCH':
        serializer.is_valid(raise_exception=True)
        serializer.save()
    return Response(s.Profile(request.user).data)


@extend_schema(request=s.Settings, responses=s.Settings)
@api_view(['GET', 'PATCH'])
def preferences(request):
    settings_record, _ = Preferences.objects.get_or_create(user=request.user)
    if request.method == 'PATCH':
        serializer = s.Settings(settings_record, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
    return Response(s.Settings(settings_record).data)


def conversation_data(item):
    return {'id': item.pk, 'title': item.title, 'created': item.created, 'updated': item.updated}


def turn_data(item):
    return {'id': item.pk, 'conversation': item.conversation_id, 'question': item.question,
            'created': item.created, 'status': item.status, 'model': item.model, 'result': item.result,
            'provenance': item.provenance, 'saved': item.saved, 'sources': exports.references(item)}


def own_turn(request, pk):
    return get_object_or_404(Turn.objects.prefetch_related('evidence'), pk=pk, conversation__owner=request.user)


@extend_schema(operation_id="list_conversations", methods=["GET"], responses=list[dict])
@extend_schema(operation_id="clear_history", methods=["DELETE"], responses={204: None})
@api_view(['GET', 'DELETE'])
def conversations(request):
    items = Conversation.objects.filter(owner=request.user)
    if request.method == 'DELETE':
        items.delete()
        return Response(status=204)
    q = request.query_params.get('q', '').strip()[:200]
    if q:
        from django.db.models import Q
        items = items.filter(Q(title__icontains=q) | Q(turns__question__icontains=q)).distinct()
    sort = 'updated' if request.query_params.get('sort') == 'oldest' else '-updated'
    return Response([conversation_data(item) for item in items.order_by(sort, 'pk')])


@extend_schema(operation_id="get_conversation", methods=["GET"], responses=dict)
@extend_schema(operation_id="rename_conversation", methods=["PATCH"], request=s.Title, responses=dict)
@extend_schema(operation_id="delete_conversation", methods=["DELETE"], responses={204: None})
@api_view(['GET', 'PATCH', 'DELETE'])
def conversation(request, pk):
    item = get_object_or_404(Conversation, pk=pk, owner=request.user)
    if request.method == 'DELETE':
        item.delete()
        return Response(status=204)
    if request.method == 'PATCH':
        item.title = validated(s.Title, request.data)['title']
        item.save(update_fields=['title', 'updated'])
    return Response({**conversation_data(item), 'turns': [
        turn_data(turn) for turn in item.turns.prefetch_related('evidence').order_by('created', 'pk')
    ]})


@extend_schema(request=s.Question, responses={201: dict})
@api_view(['POST'])
@throttle_classes([ResearchThrottle])
def ask(request):
    data = validated(s.Question, request.data)
    question = data['question']
    item = None
    previous = []
    if pk := data.get('conversation'):
        item = get_object_or_404(Conversation, pk=pk, owner=request.user)
        previous = list(reversed(item.turns.order_by('-created', '-pk').values_list('question', flat=True)[:4]))
    options, _ = Preferences.objects.get_or_create(user=request.user)
    sources = []
    provenance = {'retrieved_at': timezone.now().isoformat(), 'previous_questions': previous,
                  'generation_preferences': s.Settings(options).data, 'pipeline_version': 'round-03',
                  'citation_validation': 'Retrieved PMID membership, verbatim excerpts, numeric consistency and automated claim review. Not independent clinical validation.'}
    try:
        sources, trace = rag.retrieve(question, previous)
        provenance.update(trace)
        status, model, result = rag.synthesize(question, previous, sources, options)
        if trace.get('normalization', {}).get('notice') and not sources:
            result['message'] = trace['normalization']['notice']
    except pubmed.LiteratureError as error:
        status, model, result = 'retrieval_error', '', {'message': str(error)}
    provenance['completed_at'] = timezone.now().isoformat()
    with transaction.atomic():
        if item is None:
            item = Conversation.objects.create(owner=request.user, title=question[:180])
        else:
            item = get_object_or_404(Conversation.objects.select_for_update(), pk=item.pk, owner=request.user)
            item.save(update_fields=['updated'])
        turn = Turn.objects.create(conversation=item, question=question, status=status, model=model,
                                   result=result, provenance=provenance)
        for rank, record in enumerate(sources, 1):
            source, _ = Publication.objects.update_or_create(pmid=record['pmid'], defaults={'record': record})
            Evidence.objects.create(turn=turn, publication=source, rank=rank, snapshot=record)
    return Response(turn_data(turn), status=201)


@extend_schema(request=None, responses={201: dict, 409: dict})
@api_view(['POST'])
@throttle_classes([ResearchThrottle])
def regenerate(request, pk):
    original = own_turn(request, pk)
    if not llm.configuration()['configured']:
        return Response({'detail': 'Configure a model before generating an answer. The original research is unchanged.'}, status=409)
    options, _ = Preferences.objects.get_or_create(user=request.user)
    sources = exports.references(original)
    previous = original.provenance.get('previous_questions', [])
    status, model, result = rag.synthesize(original.question, previous, sources, options)
    provenance = {**original.provenance, 'pipeline_version': 'round-03',
                  'revision_of': original.pk, 'evidence_reused': True,
                  'generation_preferences': s.Settings(options).data,
                  'generated_at': timezone.now().isoformat(),
                  'citation_validation': 'Retrieved PMID membership, verbatim excerpts, numeric consistency and automated claim review. Not independent clinical validation.'}
    with transaction.atomic():
        # Recheck ownership/existence after the external request, e.g. concurrent deletion.
        conversation = get_object_or_404(Conversation.objects.select_for_update(),
                                        pk=original.conversation_id, owner=request.user)
        conversation.save(update_fields=['updated'])
        turn = Turn.objects.create(conversation=conversation, question=original.question,
                                   status=status, model=model, result=result, provenance=provenance)
        for entry in original.evidence.all():
            Evidence.objects.create(turn=turn, publication_id=entry.publication_id,
                                    rank=entry.rank, snapshot=entry.snapshot)
    return Response(turn_data(turn), status=201)


@extend_schema(responses=dict)
@api_view(['GET'])
def answer(request, pk):
    return Response(turn_data(own_turn(request, pk)))


@extend_schema(request=None, responses=dict)
@api_view(['PUT', 'DELETE'])
def save_answer(request, pk):
    item = own_turn(request, pk)
    item.saved = request.method == 'PUT'
    item.save(update_fields=['saved'])
    return Response({'saved': item.saved})


@extend_schema(responses=list[dict])
@api_view(['GET'])
def saved_answers(request):
    items = Turn.objects.filter(conversation__owner=request.user, saved=True).prefetch_related('evidence')
    return Response([turn_data(item) for item in items.order_by('-created')])


@extend_schema(responses=bytes)
@api_view(['GET'])
def download(request, pk, kind):
    if kind not in ('md', 'pdf', 'bib', 'csv'):
        raise Http404
    return exports.export(own_turn(request, pk), kind)


@extend_schema(operation_id="search_pubmed", parameters=[s.LiteratureQuery], responses=list[dict])
@api_view(['GET'])
@throttle_classes([LiteratureThrottle])
def articles(request):
    filters = validated(s.LiteratureQuery, request.query_params)
    term = filters.pop('q')
    try:
        if pubmed.PMID.fullmatch(term):
            records = pubmed.search(f'{term}[uid]', filters)
        elif re.fullmatch(r'10\.\d{4,9}/[^\s"\[\]]+', term, re.I):
            records = pubmed.search(f'"{term}"[aid]', filters)
        else:
            normalized = rag.normalize_query(term)
            if not normalized['normalized']:
                return Response({'detail': normalized['notice']}, status=422)
            records = pubmed.search(normalized['normalized'], filters)
    except pubmed.LiteratureError as error:
        return Response({'detail': str(error)}, status=503)
    return Response(records)


@extend_schema(responses=dict)
@api_view(['GET'])
@throttle_classes([LiteratureThrottle])
def article(request, identifier):
    if not pubmed.PMID.fullmatch(identifier):
        raise ValidationError({'pmid': 'Enter a valid PMID.'})
    cached = Publication.objects.filter(pk=identifier).first()
    if cached:
        return Response(cached.record)
    try:
        records = pubmed.records([identifier])
    except pubmed.LiteratureError as error:
        return Response({'detail': str(error)}, status=503)
    if not records:
        raise Http404
    return Response(records[0])


@extend_schema(request=s.Collection, responses=dict)
@api_view(['PUT', 'DELETE'])
@throttle_classes([LiteratureThrottle])
def save_article(request, identifier):
    if not pubmed.PMID.fullmatch(identifier):
        raise ValidationError({'pmid': 'Enter a valid PMID.'})
    if request.method == 'DELETE':
        SavedPublication.objects.filter(owner=request.user, publication_id=identifier).delete()
        return Response({'saved': False})
    data = validated(s.Collection, request.data)
    pub = Publication.objects.filter(pk=identifier).first()
    if pub is None:
        try:
            records = pubmed.records([identifier])
        except pubmed.LiteratureError as error:
            return Response({'detail': str(error)}, status=503)
        if not records:
            raise Http404
        pub, _ = Publication.objects.get_or_create(pmid=identifier, defaults={'record': records[0]})
    SavedPublication.objects.update_or_create(owner=request.user, publication=pub, defaults=data)
    return Response({'saved': True, **data})


@extend_schema(responses=list[dict])
@api_view(['GET'])
def saved_articles(request):
    items = SavedPublication.objects.filter(owner=request.user).select_related('publication').order_by('-created')
    return Response([{**row.publication.record, 'collection': row.collection} for row in items])


@extend_schema(request=s.LiteratureQuery, responses=dict)
@api_view(['GET', 'POST'])
def saved_searches(request):
    if request.method == 'POST':
        import hashlib
        import json
        data = validated(s.LiteratureQuery, request.data)
        fingerprint = hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()
        row, created = SavedSearch.objects.get_or_create(owner=request.user, fingerprint=fingerprint, defaults={'filters': data})
        return Response({'id': row.pk, 'filters': row.filters}, status=201 if created else 200)
    return Response([{'id': row.pk, 'filters': row.filters} for row in SavedSearch.objects.filter(owner=request.user).order_by('-created')])


@extend_schema(responses={204: None})
@api_view(['DELETE'])
def saved_search(request, pk):
    get_object_or_404(SavedSearch, pk=pk, owner=request.user).delete()
    return Response(status=204)
