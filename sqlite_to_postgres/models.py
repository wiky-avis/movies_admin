import uuid
from dataclasses import dataclass, field
from datetime import date, datetime
from enum import Enum
from typing import Optional


class FilmWorkType(str, Enum):
    MOVIE = "movie"
    TV_SHOW = "tv_show"


class PersonRole(str, Enum):
    DIRECTOR = "director"
    WRITER = "writer"
    ACTOR = "actor"


class TableName(str, Enum):
    FILM_WORK = "film_work"
    PERSON = "person"
    GENRE = "genre"
    GENRE_FILM_WORK = "genre_film_work"
    PERSON_FILM_WORK = "person_film_work"


@dataclass
class FilmWork:
    id: uuid.UUID
    title: str
    description: Optional[str] = None
    creation_date: Optional[date] = None
    file_path: Optional[str] = None
    rating: float = field(default=0.0)
    type: str = FilmWorkType
    created: datetime = field(default=datetime.now())
    modified: datetime = field(default=datetime.now())


@dataclass
class Person:
    id: uuid.UUID
    full_name: str
    created: datetime = field(default=datetime.now())
    modified: datetime = field(default=datetime.now())


@dataclass
class Genre:
    id: uuid.UUID
    name: str
    description: Optional[str] = None
    created: datetime = field(default=datetime.now())
    modified: datetime = field(default=datetime.now())


@dataclass
class GenreFilmWork:
    id: uuid.UUID
    film_work_id: uuid.UUID
    genre_id: uuid.UUID
    created: datetime = field(default=datetime.now())


@dataclass
class PersonFilmWork:
    id: uuid.UUID
    film_work_id: uuid.UUID
    person_id: uuid.UUID
    role: str = PersonRole
    created: datetime = field(default=datetime.now())
