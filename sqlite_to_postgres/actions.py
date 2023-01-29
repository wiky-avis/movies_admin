import logging
import sqlite3
from dataclasses import asdict, dataclass
from typing import Iterator, List

import psycopg2
from consts import CHANK
from psycopg2.extras import execute_batch

from sqlite_to_postgres.common import get_fields, get_values


class SQLiteExtractor:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.cursor = self.conn.cursor()

    def get_queries_chunk(
        self, table_name: str, model: dataclass
    ) -> Iterator[List[dataclass]]:
        self.cursor.execute(f"SELECT * FROM {table_name} ORDER BY id")
        while True:
            records = self.cursor.fetchmany(CHANK)
            if not records:
                break
            yield [model(*record) for record in records]

    def extract_movies(
        self, table_name: str, model: dataclass
    ) -> Iterator[List[dataclass]]:
        try:
            yield self.get_queries_chunk(table_name, model)
        except sqlite3.Error:
            logging.error(
                "Failed to load data from sqlite table %s",
                table_name,
                exc_info=True,
            )


class PostgresSaver:
    def __init__(self, conn):
        self.pg_conn = conn
        self.cursor = self.pg_conn.cursor()

    def save_all_data(
        self, pages: Iterator[List[dataclass]], table_name: str
    ) -> None:
        for page in pages:
            fields = ", ".join(get_fields(table_name))
            values = ", ".join(["%s" for _ in get_fields(table_name)])
            records = [
                get_values(asdict(row), table_name)
                for records in page
                for row in records
            ]
            try:
                execute_batch(
                    self.cursor,
                    f"INSERT INTO {table_name}({fields}) VALUES({values}) ON CONFLICT(id) DO NOTHING",
                    records,
                    page_size=CHANK,
                )
            except psycopg2.Error:
                logging.error(
                    "Failed to save data from postgres table %s",
                    table_name,
                    exc_info=True,
                )
        self.pg_conn.commit()
