from shivam.models import CompanyInfo
from shivam.translations import get_translator


def site_context(request):
    lang = request.session.get('language', 'en')
    if lang not in ('en', 'hi'):
        lang = 'en'

    company = CompanyInfo.objects.first()
    if not company:
        company = CompanyInfo.objects.create()

    return {
        'company': company,
        'language': lang,
        'is_hindi': lang == 'hi',
        't': get_translator(lang),
    }
