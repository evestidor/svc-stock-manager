import os
import environ
import sentry_sdk
from sentry_sdk.integrations import django


env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, []),
)

ENVIRONMENT = env('ENVIRONMENT', default='localhost')

# PATHS ----------------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ROOT_DIR_NAME = 'src.api'

PROJECT_DIR = os.path.join(BASE_DIR, ROOT_DIR_NAME)


# DJANGO SECURITY ------------------------------------------------------------

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG', default=False)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')


# DJANGO APPLICATION ---------------------------------------------------------

ROOT_URLCONF = '{}.urls'.format(ROOT_DIR_NAME)

WSGI_APPLICATION = '{}.wsgi.application'.format(ROOT_DIR_NAME)

APPEND_SLASH = True


# DJANGO APPS ----------------------------------------------------------------

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
]

LOCAL_APPS = [
    'src.api',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# DATABASE -------------------------------------------------------------------

DATABASES = {
    # reads os.environ['DATABASE_URL']
    'default': env.db(default='sqlite:///local.db'),
}


# TEMPLATES ------------------------------------------------------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# STATIC ---------------------------------------------------------------------

STATIC_URL = '/static/'


# MIDDLEWARES ----------------------------------------------------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# I18N & L10N -----------------------------------------------------------------

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# ERROR REPORTING -------------------------------------------------------------

SENTRY_DSN = env('SENTRY_DSN', default=None)

if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[django.DjangoIntegration()],
        environment=ENVIRONMENT,
    )
