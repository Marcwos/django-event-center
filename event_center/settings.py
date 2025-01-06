import os
from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary import CloudinaryImage, CloudinaryVideo
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Directorio base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad
SECRET_KEY = os.environ.get('SECRET_KEY', default='your-secret-key')
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = []

# Configuración para Render
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
ALLOWED_HOSTS.append('localhost')  # Incluye localhost para pruebas locales

# Aplicaciones instaladas
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'inicio',
    'usuarios',
    'contact',
    'servicios',
    'reservas',
    'salones',
    'cloudinary',
    'cloudinary_storage',
    'widget_tweaks',
]

# Configuración de Cloudinary
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dcdygdkwi',
    'API_KEY': '571311729757641',
    'API_SECRET': 'sw1BB5lVFvWXU3C-UlBhkKRbyjI',
}

cloudinary.config(
    cloud_name=CLOUDINARY_STORAGE['CLOUD_NAME'],
    api_key=CLOUDINARY_STORAGE['API_KEY'],
    api_secret=CLOUDINARY_STORAGE['API_SECRET']
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'event_center.urls'

# Configuración de plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'inicio/templates/inicio')],
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

WSGI_APPLICATION = 'event_center.wsgi.application'

# Base de datos (configuración para SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Localización
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_TZ = True

# Archivos estáticos
STATIC_URL = '/static/'
if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Configuración de correo SMTP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', 'default@gmail.com')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', 'password-placeholder')

DEFAULT_ADMIN_EMAIL = os.getenv('DEFAULT_ADMIN_EMAIL', 'bdhsbssj70@gmail.com')
ADMINS = [('Administrador', DEFAULT_ADMIN_EMAIL)]

# Clave de campo primario por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/usuarios/login/'
LOGOUT_REDIRECT_URL = '/'

# Modelo de usuario personalizado
AUTH_USER_MODEL = 'usuarios.CustomUser'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 1209600
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

JAZZMIN_SETTINGS = {
    "site_title": "Event Center",
    'site_header': "Centro de Eventos",
    'site_brand': "Centro de Eventos Tino Loco",
    'copyright': "tinoloco.com",
}
