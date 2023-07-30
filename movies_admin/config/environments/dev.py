import os

DEBUG = True

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost").split()

INTERNAL_IPS = [
    "127.0.0.1",
]
SHOW_COLLAPSED = True

ROLE = "dev"
