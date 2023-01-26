import uuid
from dataclasses import dataclass, field


# @dataclass(frozen=True)
@dataclass
class FilmWork:
    # Обратите внимание: для каждого поля указан тип
    title: str
    description: str
    # Ещё один бонус: в dataclass вы можете определить значение по умолчанию
    rating: float = field(default=0.0)
    id: uuid.UUID = field(default_factory=uuid.uuid4)

    # Ключевое отличие от обычных классов: вам не требуется объявлять метод __init__!
    # def __init__(self, title, description, id): сгенерируется автоматически под капотом
    # и будет соответствовать атрибутам, объявленным вами в классе


movie = FilmWork(title="movie", description="new movie", rating=0.0)
print(movie)
# Movie(title='movie', description='new movie', rating=0.0, id=UUID('6fe77164-1dfe-470d-a32d-071973759539'))
