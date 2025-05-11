# ecommerce_erp/settings/dev.py
from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']

# Backend de correo de consola para pruebas
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
