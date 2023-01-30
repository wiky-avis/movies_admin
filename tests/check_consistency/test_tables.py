import sqlite3

import psycopg2
import pytest
from psycopg2.extras import DictCursor

from tests.conftest import DSL


CLEAN_TABLES = [
    "film_work",
    "person",
    "genre",
    "genre_film_work",
    "person_film_work",
]


@pytest.mark.usefixtures("clean_table")
@pytest.mark.parametrize("clean_table", [CLEAN_TABLES], indirect=True)
def test_checking_contents_of_records_inside_tables():
    with sqlite3.connect(
        "sqlite_to_postgres/db.sqlite"
    ) as sqlite_conn, psycopg2.connect(
        **DSL, cursor_factory=DictCursor
    ) as pg_conn:
        # cursor = sqlite_conn.cursor()
        # cursor.execute("SELECT * FROM genre ORDER BY id")
        # records = cursor.fetchmany(100)
        # print("---records", records)
        cursor_2 = pg_conn.cursor()
        cursor_2.execute("SELECT * FROM genre ORDER BY id")
        records_2 = cursor_2.fetchmany(100)
        print("---records", records_2)
