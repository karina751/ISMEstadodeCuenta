"""
Django settings for mi_proyecto_django project.
...
"""

from pathlib import Path
import os 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# ...

SECRET_KEY = "django-insecure-$=k$k+mkm&%6(6zyfy@5ay-m2rzg-j+mm4!x!g@frfukqz1mcp"

DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'frontend',
    # --- CONFIGURACIÓN REACT/API (AÑADIDOS) ---
    'corsheaders',              
    'rest_framework',           
    # ------------------------------------------
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # --- CONFIGURACIÓN CORS (AÑADIDO) ---
    "corsheaders.middleware.CorsMiddleware",  # Debe ir justo aquí
    # ------------------------------------
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "mi_proyecto_django.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "mi_proyecto_django.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
# --- CONFIGURACIÓN MYSQL (REEMPLAZA LA CONFIGURACIÓN SQLITE ANTERIOR) ---

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "ism_estadocuenta_db", # <-- Nombre de la DB que debes crear
        "USER": "root",                 # <-- Usuario de MySQL
        "PASSWORD": "tu_password_mysql", # <-- REEMPLAZA ESTO con tu contraseña de MySQL
        "HOST": "localhost",            # <-- Dirección del servidor MySQL (o la del servicio en Codespace)
        "PORT": "3306",                 # <-- Puerto estándar de MySQL
        'OPTIONS': {
            # Recomendado para manejar formatos de fecha/hora y caracteres UTF-8
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}

# ------------------------------------------------------------------------


# Password validation
# ...

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# ...

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# ...

STATIC_URL = "static/"

# Default primary key field type
# ...

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# --- CONFIGURACIÓN REACT/DJANGO (FINAL) ---

# 1. Configuración CORS (Soluciona el bloqueo del navegador)
CORS_ALLOW_ALL_ORIGINS = True 


# 2. Configuración de Archivos Estáticos (Soluciona el error 404)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend/static')
]

# --------------------------------------------------------