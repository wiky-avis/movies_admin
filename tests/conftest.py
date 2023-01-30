import os
from subprocess import Popen, PIPE

import psycopg2
import pytest
from psycopg2.extras import DictCursor

from movies_admin.config.components.base import BASE_DIR
from sqlite_to_postgres.consts import DSL


def _execute_psql():
    """
    Выполняет команду psql
    """
    command = (
        f"psql "
        f"-h 127.0.0.1 "
        f"-U app "
        f"-d movies_database "
        f"-f schema_design/movies_database.ddl "
    )

    proc = Popen(command, stdout=PIPE, stderr=PIPE, env=dict(os.environ, PGPASSWORD="123qwe"), shell=True)

    stdout, stderr = proc.communicate()
    if proc.returncode:
        raise Exception("Error during running command %s: \n %s" % (command, stderr))


def _run_migrations(path_to_migrations):
    command = f"python manage.py migrate"
    proc = Popen(command, stdout=PIPE, stderr=PIPE, shell=True)
    stdout, stderr = proc.communicate()
    if proc.returncode:
        raise Exception("Error during running command %s: \n %s" % (command, stderr))


@pytest.fixture(scope="session", autouse=True)
def db(pytestconfig):
    _execute_psql()
    migration_path = os.path.join(BASE_DIR, "movies", "migrations")
    if not os.path.exists(migration_path):
        raise FileNotFoundError(f"migration path {migration_path} doesn't exist")
    _run_migrations(migration_path)


def clean_tables(*tables):
    db_conn = psycopg2.connect(**DSL, cursor_factory=DictCursor)

    for conn in db_conn:
        with conn.cursor() as cur:
            for table in tables:
                cur.execute("DELETE FROM %s" % table)
        conn.commit()
        conn.close()
