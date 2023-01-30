import pytest

from tests.vars import CLEAN_TABLES, TABLES_FIELDS


def get_count_elements_in_table(cursor, table_name) -> int:
    cursor.execute(f"SELECT COUNT(id) FROM {table_name};")
    values = cursor.fetchone()
    return values[0]


@pytest.mark.usefixtures("clean_table")
@pytest.mark.parametrize("clean_table", [CLEAN_TABLES], indirect=True)
def test_count_records_in_db(sqlite_db, pg_db):
    count_records_sqlite = [
        get_count_elements_in_table(sqlite_db, table_name)
        for table_name in TABLES_FIELDS
    ]
    count_records_pg = [
        get_count_elements_in_table(pg_db, table_name)
        for table_name in TABLES_FIELDS
    ]
    assert count_records_sqlite == count_records_pg


def get_data_from_db(cursor, fields, table_name):
    cursor.execute(f"SELECT {fields} FROM {table_name} ORDER BY id DESC;")
    for row in cursor.fetchall():
        yield row


@pytest.mark.usefixtures("clean_table")
@pytest.mark.parametrize("clean_table", [CLEAN_TABLES], indirect=True)
def test_checking_contents_of_records_inside_tables(sqlite_db, pg_db):
    for table, fields in TABLES_FIELDS.items():
        sqlite_data = get_data_from_db(sqlite_db, fields["sqlite"], table)
        pg_data = get_data_from_db(pg_db, fields["pg"], table)
        for sqlite_row, pg_row in zip(sqlite_data, pg_data):
            assert tuple(sqlite_row) == tuple(pg_data)
