import logging
from dataclasses import asdict, dataclass
from typing import AsyncGenerator

import aiosqlite
import psycopg
from common import get_fields, get_values
from consts import CHANK
from psycopg import AsyncConnection


class SQLiteExtractor:
    def __init__(self, conn: aiosqlite.connect):
        self.conn = conn

    async def get_queries_chunk(self, table_name: str, model: dataclass):
        async with self.conn.execute(
            f"SELECT * FROM {table_name} ORDER BY id"
        ) as cursor:
            while True:
                records = await cursor.fetchmany(CHANK)
                if not records:
                    break
                yield [model(*record) async for record in records]

    async def extract_movies(self, table_name: str, model: dataclass):
        try:
            await self.get_queries_chunk(table_name, model)
        except aiosqlite.Error:
            logging.error(
                "Failed to load data from sqlite table %s",
                table_name,
                exc_info=True,
            )
        finally:
            await self.conn.close()


class PostgresSaver:
    def __init__(self, conn: AsyncConnection):
        self.pg_conn = conn
        self.cursor = self.pg_conn.cursor()

    async def save_all_data(
        self, pages: AsyncGenerator, table_name: str
    ) -> None:
        async for page in pages:
            fields = ", ".join(get_fields(table_name))
            values = ", ".join(["%s" for _ in get_fields(table_name)])
            records = [
                get_values(asdict(row), table_name)
                for records in page
                for row in records
            ]
            try:
                await self.cursor.executemany(
                    f"INSERT INTO {table_name}({fields}) VALUES({values}) ON CONFLICT(id) DO NOTHING",
                    records,
                )
            except psycopg.Error:
                logging.error(
                    "Failed to save data from postgres table %s",
                    table_name,
                    exc_info=True,
                )
        await self.pg_conn.commit()
        await self.cursor.close()
