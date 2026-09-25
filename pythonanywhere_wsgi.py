# PythonAnywhere WSGI for username: shivamcompaney
# Paste into Web tab → WSGI configuration file
# (also works if account is shivamcomapney — both paths are tried)

import os
import sys

_candidates = [
    '/home/shivamcompaney/shivam_construction',
    '/home/shivamcomapney/shivam_construction',
]
path = next((p for p in _candidates if os.path.isdir(p)), _candidates[0])
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'shivam_construction.settings'
os.environ['DJANGO_DEBUG'] = 'False'
os.environ['DJANGO_ALLOWED_HOSTS'] = (
    'shivamcompaney.pythonanywhere.com,'
    'www.shivamcompaney.pythonanywhere.com,'
    'shivamcomapney.pythonanywhere.com,'
    'www.shivamcomapney.pythonanywhere.com'
)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
