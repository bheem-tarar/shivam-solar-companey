# PythonAnywhere WSGI for username: shivamcomapney
# Paste into Web tab → WSGI configuration file

import os
import sys

path = '/home/shivamcomapney/shivam_construction'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'shivam_construction.settings'
os.environ['DJANGO_DEBUG'] = 'False'
os.environ['DJANGO_ALLOWED_HOSTS'] = (
    'shivamcomapney.pythonanywhere.com,'
    'www.shivamcomapney.pythonanywhere.com'
)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
