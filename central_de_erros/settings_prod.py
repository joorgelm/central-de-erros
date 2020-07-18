from .settings import *
import dj_database_url

DEBUG = True

DATABASES = {
    'default': dj_database_url.config()
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ALLOWED_HOSTS = ['https://jlm-central-de-erros.herokuapp.com/', '.herokuapp.com/', 'jlm-central-de-erros.herokuapp.com']
