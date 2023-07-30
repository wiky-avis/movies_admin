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

# Create database schema
echo "Create database schema"
psql postgresql://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME} -f schema_design/movies_database.ddl

# Start server
echo "Starting server"
python3 movies_admin/manage.py runserver  0.0.0.0:${APP_PORT}

exec "$@"