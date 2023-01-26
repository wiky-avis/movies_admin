import psycopg2
from psycopg2.extensions import connection as _connection
from psycopg2.extras import DictCursor

from sqlite_to_postgres.models import FilmWork


def save_film_work_to_postgres(
    conn: psycopg2.extensions.connection, film_work: FilmWork
):
    pass
