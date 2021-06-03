from .base import *

DEBUG = True

INTERNAL_IPS = [
    "127.0.0.1",
]

DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.sqlite3",
    #     "NAME": os.path.join(os.path.dirname(BASE_DIR), "db.sqlite3"),
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path=referal'
        },
        'NAME': 'vzijcxwv',
        'USER': 'vzijcxwv',
        'HOST': 'satao.db.elephantsql.com',
        'PASSWORD': 'cpoctX16shRe_c6U6L56W8OS-SlxXzPU',
        'PORT': '5432',
    }
}

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 20,
}
CORS_ORIGIN_ALLOW_ALL = True
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
