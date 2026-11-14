from django.conf import settings
from django.db import models


class Preferences(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    language = models.CharField(max_length=20, default='English')
    detail = models.CharField(max_length=20, default='Standard')
    display = models.CharField(max_length=20, default='Comfortable')


class Conversation(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=180)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Publication(models.Model):
    pmid = models.CharField(max_length=12, primary_key=True)
    record = models.JSONField()


class Turn(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='turns', on_delete=models.CASCADE)
    question = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=32)
    model = models.CharField(max_length=180, blank=True)
    result = models.JSONField(default=dict)
    provenance = models.JSONField(default=dict)
    sources = models.ManyToManyField(Publication, through='Evidence')
    saved = models.BooleanField(default=False)


class Evidence(models.Model):
    turn = models.ForeignKey(Turn, related_name='evidence', on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.PROTECT)
    rank = models.PositiveSmallIntegerField()
    snapshot = models.JSONField()

    class Meta:
        ordering = ['rank']
        constraints = [models.UniqueConstraint(fields=['turn', 'publication'], name='unique_turn_publication')]


class SavedPublication(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    collection = models.CharField(max_length=80, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['owner', 'publication'], name='unique_saved_publication')]


class SavedSearch(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fingerprint = models.CharField(max_length=64)
    filters = models.JSONField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['owner', 'fingerprint'], name='unique_saved_search')]
