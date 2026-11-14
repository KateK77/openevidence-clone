import csv
import io
from pathlib import Path
from xml.sax.saxutils import escape

from django.http import HttpResponse
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import KeepTogether, Paragraph, SimpleDocTemplate, Spacer

DISCLAIMER = 'RESEARCH DEMONSTRATION — NOT FOR CLINICAL USE.'


def references(turn):
    return [entry.snapshot for entry in turn.evidence.all()]


def markdown(turn):
    lines = [f'# {turn.question}', '', DISCLAIMER, '', f'Status: {turn.status}',
             f'Date: {turn.created.isoformat()}', f'Model: {turn.model or "Unavailable"}', '',
             'Evidence scope: PubMed abstracts and metadata.', '']
    if message := turn.result.get('message'):
        lines.extend([message, ''])
    for section in turn.result.get('sections', []):
        links = ' '.join(f'[PMID {r["pmid"]}](https://pubmed.ncbi.nlm.nih.gov/{r["pmid"]}/)'
                         for r in section['citations'])
        lines.extend([f'**{section["status"].title()}** {section["text"]} {links}'.rstrip(), ''])
        lines.extend(f'> PMID {citation["pmid"]}: {citation["quote"]}' for citation in section['citations'])
        lines.append('')
    lines.extend(['## Retrieved publications', ''])
    for ref in references(turn):
        lines.append(f'- {ref["title"].rstrip(". ")}. {ref["journal"]}, {ref["date"]} ({ref.get("date_type", "publication date; type unavailable")}). [PMID {ref["pmid"]}]({ref["url"]})'
                     + (f' DOI: {ref["doi"]}' if ref['doi'] else ''))
    lines.extend(['', '## Retrieval provenance', '',
                  f'Pipeline: {turn.provenance.get("pipeline_version", "Legacy snapshot")}',
                  'Citation checks: source membership and exact abstract excerpts; clinical claim support requires review.'])
    normalization = turn.provenance.get('normalization', {})
    if normalization:
        lines.extend([f'Query mapping: {normalization.get("method", "")}',
                      f'Search terms: {normalization.get("normalized", "")}'])
    for search in turn.provenance.get('searches', []):
        lines.append(f'- {search["query"]} ({len(search["pmids"])} PMIDs)')
    return '\n'.join(lines)


def csv_cell(value):
    value = str(value or '')
    return "'" + value if value.lstrip().startswith(('=', '+', '-', '@', '\t', '\r')) else value


def bib_value(value):
    special = {'\\': r'\textbackslash{}', '{': r'\{', '}': r'\}', '&': r'\&',
               '%': r'\%', '$': r'\$', '#': r'\#', '_': r'\_', '~': r'\textasciitilde{}',
               '^': r'\textasciicircum{}'}
    return ''.join(special.get(c, c) for c in str(value).replace('\n', ' '))


def export(turn, kind):
    if kind == 'md':
        body, media = markdown(turn), 'text/markdown; charset=utf-8'
    elif kind == 'csv':
        buffer = io.StringIO()
        fields = ['pmid', 'title', 'authors', 'journal', 'year', 'doi', 'url']
        writer = csv.writer(buffer)
        writer.writerow(fields)
        for ref in references(turn):
            writer.writerow([csv_cell('; '.join(ref[k]) if k == 'authors' else ref[k]) for k in fields])
        body, media = '\ufeff' + buffer.getvalue(), 'text/csv; charset=utf-8'
    elif kind == 'bib':
        entries = []
        for ref in references(turn):
            fields = {'title': ref['title'], 'author': ' and '.join(ref['authors']),
                      'journal': ref['journal'], 'year': ref['year'], 'doi': ref['doi'], 'url': ref['url']}
            attributes = ',\n'.join(f'  {name} = {{{bib_value(value)}}}' for name, value in fields.items() if value)
            entries.append(f'@article{{pmid{ref["pmid"]},\n{attributes}\n}}')
        body, media = '\n\n'.join(entries), 'application/x-bibtex; charset=utf-8'
    else:
        buffer = io.BytesIO()
        if 'ResearchSans' not in pdfmetrics.getRegisteredFontNames():
            pdfmetrics.registerFont(TTFont('ResearchSans', str(Path(__file__).parent / 'fonts/ResearchSans-Regular.ttf')))
        styles = getSampleStyleSheet()
        for name in ['BodyText', 'Heading1', 'Heading2']:
            styles[name].fontName = 'ResearchSans'
            styles[name].leading = 16 if name == 'BodyText' else 24
            styles[name].wordWrap = 'CJK'
        style = styles['BodyText']
        story = []
        for line in markdown(turn).splitlines():
            if line:
                clean = reformat_pdf_line(line)
                selected = styles['Heading1'] if line.startswith('# ') else styles['Heading2'] if line.startswith('## ') else style
                paragraph = Paragraph(clean, selected)
                story.append(KeepTogether([paragraph]) if line.startswith('- ') else paragraph)
            else:
                story.append(Spacer(1, 6))
        def footer(canvas, doc):
            canvas.setFont('Helvetica', 8)
            canvas.drawString(44, 28, 'MedEvidence AI 2.0 | Research demonstration')
            canvas.drawRightString(doc.pagesize[0] - 44, 28, f'Page {doc.page}')
        SimpleDocTemplate(buffer, title='MedEvidence AI Research Report',
                          leftMargin=44, rightMargin=44, topMargin=42, bottomMargin=48).build(story, onFirstPage=footer, onLaterPages=footer)
        body, media = buffer.getvalue(), 'application/pdf'
    response = HttpResponse(body, content_type=media)
    response['Content-Disposition'] = f'attachment; filename="medevidence-{turn.pk}.{kind}"'
    return response


def reformat_pdf_line(line):
    import re
    line = re.sub(r'^#+ |^> |\*\*', '', line)
    line = re.sub(r'\[(PMID \d+)\]\((https://pubmed\.ncbi\.nlm\.nih\.gov/\d+/)\)', r'\1 (\2)', line)
    return escape(line)
