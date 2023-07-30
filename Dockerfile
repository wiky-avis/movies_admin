FROM python:3.11-buster

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN  apt-get update && apt-get install -y netcat && pip install --upgrade pip  \
     && apt-get install -y postgresql-client --no-install-recommends

RUN pip3 install poetry==1.5.1 --no-cache-dir

COPY poetry.lock pyproject.toml /code/

RUN poetry config virtualenvs.create false && poetry install --no-root

COPY . /code

RUN chmod +x /code/run.sh

ENTRYPOINT ["/code/run.sh"]