"""
Travis specific settings for tests
"""

from .common import *
import os

if 'CORE_API_KEY' in os.environ:
    CORE_API_KEY = os.environ['CORE_API_KEY']

if 'ROMEO_API_KEY' in os.environ:
    ROMEO_API_KEY = os.environ['ROMEO_API_KEY']

# Relative path from the project to store the uploads
MEDIA_ROOT = os.path.join(BASE_DIR, 'dissemin_media')

# Travis settings
# taken from https://gist.github.com/ndarville/3625246
DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql_psycopg2',
        'NAME':     'dissemin',
        'USER':     'postgres',
        'PASSWORD': '',
        'HOST':     'localhost',
        'PORT':     '',
    }
}

# Patch urllib3 because the default SSL module on Travis sucks
import urllib3.contrib.pyopenssl
urllib3.contrib.pyopenssl.inject_into_urllib3()