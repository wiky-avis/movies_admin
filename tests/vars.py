from sqlite_to_postgres.models import TableName


CLEAN_TABLES = [
    "film_work",
    "person",
    "genre",
    "genre_film_work",
    "person_film_work",
]


TABLES_FIELDS = {
    TableName.FILM_WORK.value: {
        "sqlite": "id,title,description,creation_date,rating,type,created_at,updated_at",
        "pg": "id,title,description,creation_date,rating,type,created,modified",
    },
    TableName.GENRE.value: {
        "sqlite": "id,name,description,created_at,updated_at",
        "pg": "id,name,description,created,modified",
    },
    TableName.PERSON.value: {
        "sqlite": "id,full_name,created_at,updated_at",
        "pg": "id,full_name,created,modified",
    },
    TableName.GENRE_FILM_WORK.value: {
        "sqlite": "id,genre_id,film_work_id,created_at",
        "pg": "id,genre_id,film_work_id,created",
    },
    TableName.PERSON_FILM_WORK.value: {
        "sqlite": "id,film_work_id,person_id,role,created_at",
        "pg": "id,film_work_id,person_id,role,created",
    },
}
