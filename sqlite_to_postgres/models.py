import uuid
from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Optional


@dataclass
class FilmWork:
    id: uuid.UUID
    title: str
    description: Optional[str] = None
    creation_date: Optional[date] = None
    rating: float = field(default=0.0)
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
    genre_id: uuid.UUID
    film_work_id: uuid.UUID
    created: datetime = field(default=datetime.now())


@dataclass
class PersonFilmWork:
    id: uuid.UUID
    person_id: uuid.UUID
    film_work_id: uuid.UUID
    role: str
    created: datetime = field(default=datetime.now())
