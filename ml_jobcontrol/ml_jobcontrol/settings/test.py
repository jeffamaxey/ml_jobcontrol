from __future__ import absolute_import

from .base import *

########## IN-MEMORY TEST DATABASE
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    },
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

########## DJANGO REST FRAMEWORK CONFIGURATION
REST_FRAMEWORK = {
    # Make json default format for tests
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}
