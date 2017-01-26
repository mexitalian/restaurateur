from __future__ import absolute_import, unicode_literals

from .base import *

SECRET_KEY = os.environ['SECRET']

DEBUG = False

ALLOWED_HOSTS = [
  '.giacomos.co.uk',
  '.giacomos.co.uk.'
]

STATIC_ROOT = '/home/giacomos/staging.giacomos.co.uk/public/static/'
# BASE_URL = 'https://charlos.co.uk'

try:
    from .local import *
except ImportError:
    pass
