import logging
import sqlite3
from dataclasses import asdict, dataclass
from typing import Any, Iterator, List, Tuple

import psycopg2
from consts import CHANK
from models import TableName
from psycopg2.extras import execute_batch


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

    def get_fields(self, table_name: str) -> List[str]:
        return {
            TableName.FILM_WORK.value: [
                "id",
                "title",
                "description",
                "creation_date",
                "rating",
                "type",
                "created",
                "modified",
                "file_path",
            ],
            TableName.GENRE.value: [
                "id",
                "name",
                "description",
                "created",
                "modified",
            ],
            TableName.PERSON.value: ["id", "full_name", "created", "modified"],
            TableName.GENRE_FILM_WORK.value: [
                "id",
                "genre_id",
                "film_work_id",
                "created",
            ],
            TableName.PERSON_FILM_WORK.value: [
                "id",
                "person_id",
                "film_work_id",
                "role",
                "created",
            ],
        }.get(table_name)

    def get_values(self, row: dict, table_name: str) -> Tuple[Any]:
        return tuple(row[field] for field in self.get_fields(table_name))

    def save_all_data(
        self, pages: Iterator[List[dataclass]], table_name: str
    ) -> None:
        for page in pages:
            fields = ", ".join(self.get_fields(table_name))
            values = ", ".join(["%s" for _ in self.get_fields(table_name)])
            records = [
                self.get_values(asdict(row), table_name)
                for records in page
                for row in records
            ]
            try:
                execute_batch(
                    self.cursor,
                    f"INSERT INTO {table_name}({fields}) VALUES({values})",
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
