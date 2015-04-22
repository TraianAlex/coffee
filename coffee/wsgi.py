"""
WSGI config for coffee project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coffee.settings")

ON_HEROKU = False

if ON_HEROKU == True:
	from dj_static import Cling
	application = Cling(get_wsgi_application())
else:
	application = get_wsgi_application()