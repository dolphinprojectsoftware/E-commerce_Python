# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-esctco3prky5wi+o$ae4507av=ypw=s*g82%o2tal_%0kxm809'

#Allowed Host
ALLOWED_HOSTS = []


#ruta principal
ROOT_URLCONF = 'core.urls'


#config wsgi
WSGI_APPLICATION = 'core.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
