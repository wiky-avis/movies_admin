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
    "dbname": "movies_database",
    "user": "app",
    "password": "123qwe",
    "host": "127.0.0.1",
    "port": 5432,
}
