# Paste this into PythonAnywhere Web tab → WSGI configuration file
# Path is usually: /var/www/shivamcompaney_pythonanywhere_com_wsgi.py

import os
import sys

path = '/home/shivamcompaney/shivam_construction'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'shivam_construction.settings'
os.environ['DJANGO_DEBUG'] = 'False'
os.environ['DJANGO_ALLOWED_HOSTS'] = (
    'shivamcompaney.pythonanywhere.com,'
    'www.shivamcompaney.pythonanywhere.com'
)

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
