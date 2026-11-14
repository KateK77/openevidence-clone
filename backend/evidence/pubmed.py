import hashlib
import re
import threading
import time

import requests
from defusedxml import ElementTree
from defusedxml.common import DefusedXmlException
from django.conf import settings
from django.core.cache import cache

BASE = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils'
PMID = re.compile(r'[1-9][0-9]{0,11}')
TYPES = ('Clinical Trial', 'Randomized Controlled Trial', 'Review', 'Systematic Review', 'Meta-Analysis')
_lock = threading.Lock()
_last_request = 0.0


class LiteratureError(Exception):
    pass


def fetch(endpoint, **params):
    global _last_request
    key = 'pubmed:' + hashlib.sha256(repr((endpoint, sorted(params.items()))).encode()).hexdigest()
    cached = cache.get(key)
    if cached is not None:
        return cached
    options = {'db': 'pubmed', 'tool': 'medevidence_ai', **params}
    if settings.NCBI_EMAIL:
        options['email'] = settings.NCBI_EMAIL
    if settings.NCBI_API_KEY:
        options['api_key'] = settings.NCBI_API_KEY
    try:
        with _lock:
            interval = 0.11 if settings.NCBI_API_KEY else 0.35
            time.sleep(max(0, interval - (time.monotonic() - _last_request)))
            _last_request = time.monotonic()
        response = requests.get(f'{BASE}/{endpoint}.fcgi', params=options, timeout=(4, 12))
        if response.status_code == 429:
            raise LiteratureError('PubMed request limit reached. Try again shortly.')
        response.raise_for_status()
        if len(response.content) > 8_000_000:
            raise LiteratureError('PubMed returned an unexpectedly large response.')
    except requests.Timeout:
        raise LiteratureError('PubMed timed out. Try again shortly.') from None
    except requests.RequestException:
        raise LiteratureError('PubMed is temporarily unavailable.') from None
    cache.set(key, response.content, 1800)
    return response.content


def node_text(node):
    return ''.join(node.itertext()).strip() if node is not None else ''


def records(ids):
    ids = [str(pmid) for pmid in ids if PMID.fullmatch(str(pmid))]
    if not ids:
        return []
    try:
        root = ElementTree.fromstring(fetch('efetch', id=','.join(ids), retmode='xml'))
    except (SyntaxError, ValueError, DefusedXmlException):
        raise LiteratureError('PubMed returned an invalid article response.') from None
    if root.tag != 'PubmedArticleSet' or root.find('.//ERROR') is not None:
        raise LiteratureError('PubMed returned an invalid article response.')
    output = []
    for item in root.findall('PubmedArticle'):
        pmid = item.findtext('MedlineCitation/PMID', '')
        article = item.find('MedlineCitation/Article')
        if pmid not in ids or article is None:
            continue
        date_node = article.find('ArticleDate')
        if date_node is None:
            date_node = article.find('Journal/JournalIssue/PubDate')
        date = ''
        if date_node is not None:
            date = ' '.join(filter(None, (date_node.findtext(k) for k in ('Year', 'Month', 'Day'))))
            date = date or date_node.findtext('MedlineDate', '')
        year = re.search(r'\b\d{4}\b', date)
        authors = []
        for author in article.findall('AuthorList/Author'):
            name = author.findtext('CollectiveName') or ' '.join(
                filter(None, (author.findtext('ForeName'), author.findtext('LastName')))
            )
            if name:
                authors.append(name)
        sections = []
        for section in article.findall('Abstract/AbstractText'):
            if value := node_text(section):
                label = section.get('Label')
                sections.append(f'{label}: {value}' if label else value)
        output.append({
            'pmid': pmid, 'title': node_text(article.find('ArticleTitle')), 'authors': authors,
            'journal': article.findtext('Journal/Title', ''), 'date': date,
            'year': int(year.group()) if year else None, 'abstract': '\n\n'.join(sections),
            'types': [node_text(t) for t in article.findall('PublicationTypeList/PublicationType')],
            'doi': item.findtext('PubmedData/ArticleIdList/ArticleId[@IdType="doi"]', ''),
            'url': f'https://pubmed.ncbi.nlm.nih.gov/{pmid}/',
        })
    return output


def search_ids(term, limit=16, sort='relevance'):
    import json
    try:
        data = json.loads(fetch('esearch', term=term, retmode='json', retmax=limit, sort=sort))
        ids = data['esearchresult']['idlist']
        if not isinstance(ids, list) or any(not isinstance(id_, str) or not PMID.fullmatch(id_) for id_ in ids):
            raise ValueError
        return ids
    except (KeyError, ValueError, TypeError):
        raise LiteratureError('PubMed returned an invalid search response.') from None


def filter_term(term, filters):
    clauses = [f'({term})']
    for key, field in [('year', 'dp'), ('journal', 'jour'), ('article_type', 'pt')]:
        if value := filters.get(key):
            value = str(value).replace('"', ' ').replace('[', ' ').replace(']', ' ')
            clauses.append(f'"{value}"[{field}]')
    if filters.get('free'):
        clauses.append('free full text[sb]')
    return ' AND '.join(clauses)


def search(term, filters):
    ids = search_ids(filter_term(term, filters), sort=filters.get('sort', 'relevance'))
    by_id = {article['pmid']: article for article in records(ids)}
    return [by_id[pmid] for pmid in dict.fromkeys(ids) if pmid in by_id]
