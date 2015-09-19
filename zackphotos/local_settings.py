"""
For use with dev server
To run using these settings:

export DJANGO_SETTINGS_MODULE=zackphotos.local_settings
python manage.py runserver 0.0.0.0:8000
	
"""

from .settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0xh2)_o(e)#i8fi9k(4_b^k^12!*7_$cl)b2ld*p-!&-k3d2in'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
THUMBNAIL_DEBUG = True

ALLOWED_HOSTS = ['10.0.0.19']

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'photogallery',
        'USER': 'photogallery',
        'PASSWORD': 'K9Y$%qWU-%a;Nk"g',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Static Files

STATIC_ROOT = ''
STATIC_URL = '/assets/'
STATICFILES_DIRS = (
    # os.path.join(BASE_DIR, "static"),
)