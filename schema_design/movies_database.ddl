CREATE SCHEMA IF NOT EXISTS content;

CREATE TABLE IF NOT EXISTS content.film_work (
    id uuid PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    creation_date DATE,
    rating FLOAT,
    type TEXT not null,
    created timestamp with time zone,
    modified timestamp with time zone
);
CREATE UNIQUE INDEX film_work_title ON content.film_work (id, title, creation_date);

CREATE TABLE IF NOT EXISTS content.person (
    id uuid PRIMARY KEY,
    full_name TEXT NOT NULL,
    created timestamp with time zone,
    modified timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.genre (
    id uuid PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    created timestamp with time zone,
    modified timestamp with time zone
);
CREATE UNIQUE INDEX film_work_genre ON content.genre (id, name);

CREATE TABLE IF NOT EXISTS content.genre_film_work (
    id uuid PRIMARY KEY,
    genre_id uuid NOT NULL REFERENCES content.genre (id) ON UPDATE CASCADE ON DELETE CASCADE,
    film_work_id uuid NOT NULL REFERENCES content.film_work (id) ON UPDATE CASCADE ON DELETE CASCADE,
    created timestamp with time zone
);
CREATE UNIQUE INDEX film_work_genre_idx ON content.genre_film_work (film_work_id, genre_id);

CREATE TABLE IF NOT EXISTS content.person_film_work (
    id uuid PRIMARY KEY,
    person_id uuid NOT NULL REFERENCES content.person (id) ON UPDATE CASCADE ON DELETE CASCADE,
    film_work_id uuid NOT NULL REFERENCES content.film_work (id) ON UPDATE CASCADE ON DELETE CASCADE,
    role TEXT NOT NULL,
    created timestamp with time zone
);
CREATE UNIQUE INDEX film_work_person_idx ON content.person_film_work (film_work_id, person_id);
