from split_settings.tools import include


include(
    "../components/database.py",
    "../components/common.py",
    "../components/base.py",
)

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]

INTERNAL_IPS = [
    "127.0.0.1",
]
SHOW_COLLAPSED = True

ROLE = "dev"
