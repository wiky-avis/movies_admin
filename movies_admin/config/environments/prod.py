import os

from split_settings.tools import include


include("../components/database.py", "../components/base.py")

DEBUG = os.environ.get("DEBUG", False)

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", [])

ROLE = "prod"
