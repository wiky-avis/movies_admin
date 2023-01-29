import sqlite3

import psycopg2
from actions import PostgresSaver, SQLiteExtractor
from consts import DSL, MODELS, TABLES
from psycopg2.extensions import connection as _connection
from psycopg2.extras import DictCursor


def load_from_sqlite(connection: sqlite3.Connection, pg_conn: _connection):
    """Основной метод загрузки данных из SQLite в Postgres"""
    for table_name, model in zip(TABLES, MODELS):
        sqlite_extractor = SQLiteExtractor(connection)
        data = sqlite_extractor.extract_movies(table_name, model)
        postgres_saver = PostgresSaver(pg_conn)
        postgres_saver.save_all_data(data, table_name)


if __name__ == "__main__":
    with sqlite3.connect("db.sqlite") as sqlite_conn, psycopg2.connect(
        **DSL, cursor_factory=DictCursor
    ) as pg_conn:
        load_from_sqlite(sqlite_conn, pg_conn)
