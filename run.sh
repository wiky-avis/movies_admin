#!/usr/bin/env bash

set -e

if [ "${DATABASE}" = "Postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z ${POSTGRES_HOST} ${POSTGRES_PORT}; do
      sleep 0.1
    done

    echo "PostgreSQL started"

fi

# Migrations
psql -h 127.0.0.1 -U app -d movies_database -f schema_design/movies_database.ddl
python3 movies_admin/manage.py migrate --fake-initial --settings=config.settings
cd sqlite_to_postgres && python3 load_data.py
cd ..

# Start server
echo "Starting server"
python3 movies_admin/manage.py runserver  0.0.0.0:8000
