from django import template

from shivam.bilingual import localized_designation, localized_value

register = template.Library()


@register.simple_tag(takes_context=True)
def project_status_label(context, status_code):
    return context['t'].project_status(status_code)


@register.simple_tag(takes_context=True)
def lfield(context, obj, field, fallback_key=''):
    lang = context.get('language', 'en')
    value = localized_value(obj, field, lang)
    if (not value or not str(value).strip()) and fallback_key:
        return context['t'].get(fallback_key, '')
    return value


@register.filter
def t_category(value, translator):
    if hasattr(translator, 'service_category'):
        return translator.service_category(value)
    return value


@register.filter
def t_doc_type(value, translator):
    if hasattr(translator, 'document_type'):
        return translator.document_type(value)
    return value


@register.filter
def t_designation(value, lang):
    return localized_designation(value, lang if isinstance(lang, str) else 'en')


@register.simple_tag(takes_context=True)
def tdesig(context, text):
    return localized_designation(text, context.get('language', 'en'))
