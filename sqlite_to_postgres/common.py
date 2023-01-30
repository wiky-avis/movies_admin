from typing import Any, List, Tuple

from models import TableName


def get_fields(table_name: str) -> List[str]:
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


def get_values(row: dict, table_name: str) -> Tuple[Any]:
    return tuple(row[field] for field in get_fields(table_name))
