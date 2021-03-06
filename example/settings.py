"""
Django settings for app project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, re
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from django.utils.translation import ugettext_lazy as _


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'YOUR_SECRET_KEY'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SERVE_MEDIA = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'django.contrib.messages',

    'suit',
    'fluentcms_suit',
    'django.contrib.admin',

    'fluent_pages',
    'fluent_pages.pagetypes.flatpage',
    'fluent_pages.pagetypes.fluentpage',
    # 'fluent_pages.pagetypes.redirectnode',  # upstream bug #110
    'fluent_pages.pagetypes.textfile',

    'mptt',
    'polymorphic',
    'polymorphic_tree',
    'slug_preview',
    'parler',

    'fluent_contents',
    'fluent_contents.plugins.code',
    'fluent_contents.plugins.commentsarea',
    'fluent_contents.plugins.gist',
    'fluent_contents.plugins.googledocsviewer',
    'fluent_contents.plugins.iframe',
    'fluent_contents.plugins.markup',
    'fluent_contents.plugins.oembeditem',
    'fluent_contents.plugins.picture',
    'fluent_contents.plugins.rawhtml',
    'fluent_contents.plugins.sharedcontent',
    'fluent_contents.plugins.text',

    'any_urlfield',
    'any_imagefield',

    'django_wysiwyg',
    'tinymce',
]

import django
if django.VERSION < (1, 7):
    INSTALLED_APPS += [
        'south',
    ]

if 'fluent_contents.plugins.commentsarea' in INSTALLED_APPS:
    if django.VERSION < (1, 7):
        INSTALLED_APPS += [
            'django.contrib.comments',
        ]
    else:
        INSTALLED_APPS += [
            'django_comments',
        ]

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.middleware.security.SecurityMiddleware',
]

ROOT_URLCONF = 'example.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(os.path.dirname(__file__), 'templates'),
            os.path.join(os.path.dirname(__file__), 'templates', 'layouts'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.core.context_processors.debug',
                'django.core.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

SITE_ID = 1

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', _('English')),
    ('es', _('Spanish')),
    ('fr', _('French')),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')

STATIC_URL = '/static/'

## Fluent / Parler settings

FLUENT_PAGES_TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates', 'layouts')
FLUENT_PAGES_PARENT_ADMIN_MIXIN = 'fluentcms_suit.admin.FluentPagesParentAdminMixin'

DJANGO_WYSIWYG_FLAVOR = "tinymce"

PARLER_DEFAULT_LANGUAGE = LANGUAGE_CODE
PARLER_LANGUAGES = {
    SITE_ID: tuple([{'code': lang[0]} for lang in LANGUAGES]),
    'default': {
        'fallback': LANGUAGE_CODE,
        'hide_untranslated': False,
    }
}
