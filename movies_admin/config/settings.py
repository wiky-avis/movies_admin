from os import environ

from split_settings.tools import include


ROLE = environ.get("ROLE") or "dev"

base_settings = [
    "components/base.py",
    "components/database.py",
    "environments/{0}.py".format(ROLE),
]

include(*base_settings)
