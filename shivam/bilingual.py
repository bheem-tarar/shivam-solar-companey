"""Helpers for English / Hindi content on models."""

from shivam.translations import DESIGNATION_HI


def localized_value(obj, field, lang='en'):
    if obj is None:
        return ''
    if lang == 'hi':
        hi_val = getattr(obj, f'{field}_hi', None)
        if hi_val and str(hi_val).strip():
            return hi_val
    val = getattr(obj, field, None)
    val = '' if val is None else val
    if lang == 'hi' and field == 'designation' and val:
        return localized_designation(val, lang)
    if lang == 'hi' and field == 'category' and val:
        return DESIGNATION_HI.get(val, val)
    return val


def localized_designation(text, lang='en'):
    if not text:
        return ''
    if lang == 'hi':
        return DESIGNATION_HI.get(text, text)
    return text


def localized_category(text, lang='en', translator=None):
    if translator and hasattr(translator, 'service_category'):
        return translator.service_category(text)
    return text
