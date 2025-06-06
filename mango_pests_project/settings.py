# mango_pests_project/settings.py

from pathlib import Path

# ─── BUILD PATHS ───────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent


# ─── SECURITY / DEBUG ───────────────────────────
SECRET_KEY = 'django-insecure-l=u882t)6xdp59@am8(y5kpw7q2gv&@+3as1wwl9%%6arx9dbo'


DEBUG = True

ALLOWED_HOSTS = []


# ─── APPLICATION DEFINITION ─────────────
INSTALLED_APPS = [
    # Default Django apps...
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third‐party
    'django_bootstrap5',

    # our apps
    'mango_pests',
    'growers',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mango_pests_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            
            
        ],
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

WSGI_APPLICATION = 'mango_pests_project.wsgi.application'


# ─── DATABASE ─────────────────────────────
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db_experiment.sqlite3',

    }
}


# ─── PASSWORD VALIDATION ──────────────────
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]





LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# ─── STATIC FILES ────────────────────────────────────────────────────────────────
#   a) STATIC_ROOT: where ‘collectstatic’ will gather everything (usually for deployment).
STATIC_URL = '/static/'


STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    
]




# ─── DEFAULT PRIMARY KEY FIELD TYPE ───────────────────
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ─── LOGIN/LOGOUT REDIRECTS ────────────────
LOGIN_REDIRECT_URL = '/growers/profile/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = "/growers/login"
