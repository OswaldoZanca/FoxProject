# ecommerce_erp/settings/prod.py
from .base import *
from decouple import config, Csv

DEBUG = False
# ALLOWED_HOSTS ya viene desde el .env pero puedes forzarlo
# ALLOWED_HOSTS = ['miapp.com', 'api.miapp.com']

# Seguridad adicional en producción
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Emails críticos
ADMINS = [('Admin', 'admin@miapp.com')]
SERVER_EMAIL = 'noreply@miapp.com'

# Backend real de correo (reemplaza con tu SMTP)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST', default='smtp.miapp.com')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_USER', default='user@miapp.com')
EMAIL_HOST_PASSWORD = config('EMAIL_PASS', default='password')
