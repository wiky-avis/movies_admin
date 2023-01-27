import os

from django.core.wsgi import get_wsgi_application

from movies_admin.config.components.base import CONFIG_PATH


os.environ.setdefault("DJANGO_SETTINGS_MODULE", CONFIG_PATH)

application = get_wsgi_application()
