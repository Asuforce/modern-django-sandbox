from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='local_secret_key')

DEBUG = env.bool('DJANGO_DEBUG', default=True)
