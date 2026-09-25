#!/bin/bash
# Run this inside PythonAnywhere Bash after: workon shivam-env
set -e
cd ~/shivam_construction || cd ~/shivam_construction_companey || exit 1
pip install whitenoise==6.9.0
python << 'PY'
from pathlib import Path
p = Path('shivam_construction/settings.py')
t = p.read_text()
if 'whitenoise.middleware.WhiteNoiseMiddleware' not in t:
    t = t.replace(
        "'django.middleware.security.SecurityMiddleware',",
        "'django.middleware.security.SecurityMiddleware',\n    'whitenoise.middleware.WhiteNoiseMiddleware',",
        1,
    )
if 'CompressedStaticFilesStorage' not in t:
    insert = '''
STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedStaticFilesStorage"},
}
'''
    if 'MEDIA_URL' in t and 'STORAGES' not in t:
        t = t.replace('MEDIA_URL = ', insert + '\nMEDIA_URL = ', 1)
p.write_text(t)
print('settings patched')
PY
python manage.py collectstatic --noinput
echo "DONE. Now Web tab -> Reload"
echo "Also set Static files:"
echo "  /static/ -> $HOME/shivam_construction/staticfiles"
ls -la staticfiles/css/style.css || ls -la static/css/style.css
