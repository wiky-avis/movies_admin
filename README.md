# Admin panel

Описание структуры и порядок выполнения проекта:
1. `schema_design` - раздел c материалами для архитектуры базы данных.
2. `movies_admin` - раздел с материалами для панели администратора.
3. `sqlite_to_postgres` - раздел с материалами по миграции данных.

## Установка зависимостей
```bash
pip install poetry==1.1.13
poetry install --no-root && poetry shell
```

## Создание схемы и таблиц в БД
```bash
psql -h 127.0.0.1 -U app -d movies_database -f schema_design/movies_database.ddl
```

## Применение миграций
```bash
python3 movies_admin/manage.py migrate --settings=config.settings
```

## Перенос данных из sqlite в postgres
```bash
cd sqlite_to_postgres && python3 load_data.py
```

## Прогнать линтеры
```bash
make linters
```

## Тестирование
Поднять контейнер c БД Postgres
```bash
docker run -d \
  --name postgres \
  -p 5432:5432 \
  -v $HOME/postgresql/data:/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD=123qwe \
  -e POSTGRES_USER=app \
  -e POSTGRES_DB=movies_database  \
  postgres:13
```
Запустить тесты
```bash
pytest
```
