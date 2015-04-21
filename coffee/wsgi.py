"""
WSGI config for coffee project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coffee.settings")

from dj_static import Cling
application = Cling(get_wsgi_application())

#application = get_wsgi_application()

#web: gunicorn coffee.wsgi --log-file -
#web: python manage.py runserver 0.0.0.0:8000