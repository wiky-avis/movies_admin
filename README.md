# Greetings traveller

Описание структуры и порядок выполнения проекта:
1. `schema_design` - раздел c материалами для архитектуры базы данных.
2. `movies_admin` - раздел с материалами для панели администратора.
3. `sqlite_to_postgres` - раздел с материалами по миграции данных.

# Установка зависимостей
```bash
pip install poetry==1.1.13
poetry install --no-root && poetry shell
```

# Создание схемы и таблиц в БД
```bash
psql -h 127.0.0.1 -U app -d movies_database -f schema_design/movies_database.ddl
```

# Применение миграций
```bash
python movies_admin/manage.py migrate
```

# Перенос данных из sqlite в postgres
```bash
python sqlite_to_postgres/load_data.py
```

# Прогнать линтеры
```bash
make linters
```
