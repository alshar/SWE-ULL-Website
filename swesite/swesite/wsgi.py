"""
WSGI config for swesite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/

wsgi.py is used to help your Django application communicate with the web server. You can treat this as boilerplate.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'swesite.settings')

application = get_wsgi_application()
