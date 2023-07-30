import asyncio
import sqlite3

import aiosqlite
import psycopg
from actions import PostgresSaver, SQLiteExtractor
from consts import DSL, MODELS, TABLES
from psycopg import AsyncConnection


async def load_from_sqlite(
    connection: sqlite3.Connection, pg_conn: AsyncConnection
):
    """Основной метод загрузки данных из SQLite в Postgres"""
    for table_name, model in zip(TABLES, MODELS):
        sqlite_extractor = SQLiteExtractor(connection)
        data = await sqlite_extractor.extract_movies(table_name, model)
        postgres_saver = PostgresSaver(pg_conn)
        await postgres_saver.save_all_data(data, table_name)


async def run():
    async with aiosqlite.connect(
        "db.sqlite"
    ) as sqlite_conn, psycopg.AsyncConnection.connect(**DSL) as pg_conn:
        sqlite_conn.row_factory = aiosqlite.Row
        await load_from_sqlite(sqlite_conn, pg_conn)


if __name__ == "__main__":
    asyncio.run(run())
