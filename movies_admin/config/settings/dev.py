from .base import *


DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]

INSTALLED_APPS.append("debug_toolbar")
MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")
INTERNAL_IPS = [
    "127.0.0.1",
]
SHOW_COLLAPSED = True

ROLE = "dev"
