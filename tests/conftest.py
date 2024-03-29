import os
import sqlite3
from subprocess import PIPE, Popen

import psycopg2
import pytest
from psycopg2.extras import DictCursor


DSL = {
    "dbname": "movies_database",
    "user": "app",
    "password": "123qwe",
    "host": "127.0.0.1",
    "port": 6667,
}


def _execute_psql():
    command = (
        "psql "
        "-h 127.0.0.1 "
        "-p 6667 "
        "-U app "
        "-d movies_database "
        "-f schema_design/movies_database.ddl "
    )
    proc = Popen(
        command,
        stdout=PIPE,
        stderr=PIPE,
        env=dict(os.environ, PGPASSWORD="123qwe"),
        shell=True,
    )
    stdout, stderr = proc.communicate()
    if proc.returncode:
        raise Exception(
            "Error during running command %s: \n %s" % (command, stderr)
        )


def _run_migrations():
    command = "python3 movies_admin/manage.py migrate --fake-initial --settings=config.settings"
    proc = Popen(command, stdout=PIPE, stderr=PIPE, shell=True)
    stdout, stderr = proc.communicate()
    if proc.returncode:
        raise Exception(
            "Error during running command %s: \n %s" % (command, stderr)
        )


def _load_test_data():
    command = ("cd sqlite_to_postgres && python3 load_data.py",)
    proc = Popen(command, stdout=PIPE, stderr=PIPE, shell=True)
    stdout, stderr = proc.communicate()
    if proc.returncode:
        raise Exception(
            "Error during running command %s: \n %s" % (command, stderr)
        )


@pytest.fixture(scope="session", autouse=True)
def db(pytestconfig):
    _execute_psql()
    _run_migrations()
    _load_test_data()


def clean_tables(*tables):
    pg_conn = psycopg2.connect(**DSL, cursor_factory=DictCursor)
    if pg_conn:
        with pg_conn.cursor() as cur:
            for table in tables:
                cur.execute("DELETE FROM %s" % table)
        pg_conn.commit()
        pg_conn.close()


@pytest.fixture
def clean_table(request):
    def teardown():
        clean_tables(*request.param)

    request.addfinalizer(teardown)


@pytest.fixture
def sqlite_db():
    with sqlite3.connect("sqlite_to_postgres/db.sqlite") as sqlite_conn:
        yield sqlite_conn.cursor()


@pytest.fixture
def pg_db():
    with psycopg2.connect(**DSL, cursor_factory=DictCursor) as pg_conn:
        yield pg_conn.cursor()
