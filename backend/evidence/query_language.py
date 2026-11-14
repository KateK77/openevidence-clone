"""A bounded terminology aid, not a general-purpose medical translator.

Unrecognized Chinese text is never silently dropped from a clinical query.
The returned transformation is stored with each answer for inspection.
"""
import re

TERMS = {
    '2型糖尿病': 'type 2 diabetes mellitus', '二型糖尿病': 'type 2 diabetes mellitus',
    '1型糖尿病': 'type 1 diabetes mellitus', '糖尿病': 'diabetes mellitus', '高血压': 'hypertension',
    '肥胖症': 'obesity', '肥胖': 'obesity', '减重': 'weight loss', '超重': 'overweight',
    '心力衰竭': 'heart failure', '心衰': 'heart failure', '冠心病': 'coronary artery disease',
    '慢性肾病': 'chronic kidney disease', '肾病': 'kidney disease', '肾衰竭': 'kidney failure',
    '司美格鲁肽': 'semaglutide', '替尔泊肽': 'tirzepatide', '二甲双胍': 'metformin',
    '胰岛素': 'insulin', '受体激动剂': 'receptor agonists', '受体': 'receptor',
    '抑制剂': 'inhibitors', '阿司匹林': 'aspirin', '他汀': 'statins',
    '随机对照试验': 'randomized controlled trial', '系统综述': 'systematic review',
    '荟萃分析': 'meta-analysis', '不良反应': 'adverse effects', '副作用': 'adverse effects',
    '局限性': 'limitations', '局限': 'limitations', '安全性': 'safety', '风险': 'risks',
    '有效性': 'efficacy', '疗效': 'efficacy', '治疗': 'treatment', '预防': 'prevention',
    '诊断': 'diagnosis', '证据': 'evidence', '研究': 'studies', '对比': 'comparison',
    '比较': 'comparison', '成人': 'adults', '儿童': 'children', '青少年': 'adolescents',
    '老年人': 'elderly', '孕妇': 'pregnancy', '妊娠': 'pregnancy', '疼痛': 'pain',
    '头痛': 'headache', '哮喘': 'asthma', '抑郁症': 'depression', '肺癌': 'lung cancer',
    '乳腺癌': 'breast cancer', '卒中': 'stroke', '中风': 'stroke', '失眠': 'insomnia',
    '不能': 'cannot', '不推荐': 'not recommended', '禁忌': 'contraindications',
    '这些': 'these', '它们': 'they', '相比': 'versus', '与': 'and', '和': 'and',
}
FILLER = re.compile(r'请问|请|怎么|如何|什么|哪些|有没有|是否|可以|的|有|是|吗|呢|在|对于|关于|用于|中')
HAN = re.compile(r'[\u3400-\u9fff]')


def normalize_query(question):
    original = question.strip()
    if not HAN.search(original):
        return {'original': original, 'normalized': original, 'method': 'original', 'notice': ''}
    text = original
    for source in sorted(TERMS, key=len, reverse=True):
        text = text.replace(source, ' ' + TERMS[source] + ' ')
    text = FILLER.sub(' ', text)
    if HAN.search(text):
        return {'original': original, 'normalized': '', 'method': 'unmapped Chinese terms',
                'notice': 'Some Chinese terms could not be mapped reliably. Please include English medical keywords or a PMID. This is a query translation limitation, not evidence that no studies exist.'}
    normalized = re.sub(r'\s+', ' ', re.sub(r'[，。！？、：；]', ' ', text)).strip()
    return {'original': original, 'normalized': normalized, 'method': 'Chinese terminology glossary',
            'notice': 'Chinese terms were mapped using a limited terminology glossary. Review the English search terms in retrieval provenance.'}
