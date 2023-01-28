import os


DEBUG = os.environ.get("DEBUG", False)

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", [])

ROLE = "prod"
