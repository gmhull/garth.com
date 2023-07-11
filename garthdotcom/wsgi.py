"""
WSGI config for garthdotcom project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os, sys
from django.core.wsgi import get_wsgi_application

path = '/home/gmhull/garthdotcom'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'garthdotcom.settings')

application = get_wsgi_application()
