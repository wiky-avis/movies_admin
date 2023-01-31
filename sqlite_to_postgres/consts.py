import os

from models import (
    FilmWork,
    Genre,
    GenreFilmWork,
    Person,
    PersonFilmWork,
    TableName,
)


CHANK = 100

TABLES = (
    TableName.FILM_WORK.value,
    TableName.GENRE.value,
    TableName.PERSON.value,
    TableName.GENRE_FILM_WORK.value,
    TableName.PERSON_FILM_WORK.value,
)

MODELS = (
    FilmWork,
    Genre,
    Person,
    GenreFilmWork,
    PersonFilmWork,
)

DSL = {
    "dbname": os.environ.get("DB_NAME", "movies_database"),
    "user": os.environ.get("DB_USER", "app"),
    "password": os.environ.get("DB_PASSWORD", "123qwe"),
    "host": os.environ.get("HOST", "127.0.0.1"),
    "port": os.environ.get("PORT", 5432),
}
