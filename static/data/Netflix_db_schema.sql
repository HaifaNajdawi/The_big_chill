--Drop existing tables
DROP TABLE "Netflix_title_Listed_in";
DROP TABLE "Netflix_Listed_in";
DROP TABLE "OMDB_title_genre";
DROP TABLE "OMDB_genre";
DROP TABLE "OMDB_title_language";
DROP TABLE "OMDB_language";
DROP TABLE "title_cast";
DROP TABLE "cast";
DROP TABLE "Title";

-- Schema Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- merged OMDB and Netflix attributes into Title table
CREATE TABLE "Title" (
    -- Netflix
    "show_id" int   NOT NULL,
    -- Netflix
    "title" varchar   NOT NULL,
    -- Netflix
    "type" varchar,
    -- Netflix
    "director" varchar,
    -- Netflix
    "country" varchar,
    -- Netflix
    "date_added" date,
    -- Netflix
    "rating" varchar,
    -- Netflix
    "duration" varchar,
    -- Netflix
    "description" varchar,
    -- Netflix
    "release_year" int,
    -- OMDB
    "runtime" varchar,
    -- OMDB
    "imdbRating" float,
    -- OMDB
    "imdbVotes" int,
    -- OMDB
    "poster" varchar,
    -- OMDB
    "awards" varchar,
    -- OMDB
    "boxoffice" varchar,
    CONSTRAINT "pk_Title" PRIMARY KEY (
        "show_id"
     )
);

CREATE TABLE "OMDB_genre" (
    "omdb_genre_no" int   NOT NULL,
    "omdb_genre" varchar   NOT NULL,
    CONSTRAINT "pk_OMDB_genre" PRIMARY KEY (
        "omdb_genre_no"
     )
);

CREATE TABLE "OMDB_title_genre" (
    "omdb_genre_no" int   NOT NULL,
    "show_id" int   NOT NULL,
    CONSTRAINT "pk_OMDB_title_genre" PRIMARY KEY (
        "omdb_genre_no","show_id"
     )
);

CREATE TABLE "Netflix_title_Listed_in" (
    "netflix_genre_no" int   NOT NULL,
    "show_id" int   NOT NULL,
    CONSTRAINT "pk_Netflix_title_Listed_in" PRIMARY KEY (
        "netflix_genre_no","show_id"
     )
);

CREATE TABLE "Netflix_Listed_in" (
    "netflix_genre_no" int   NOT NULL,
    "netflix_genre" varchar   NOT NULL,
    CONSTRAINT "pk_Netflix_Listed_in" PRIMARY KEY (
        "netflix_genre_no"
     )
);

CREATE TABLE "OMDB_language" (
    "language_no" int   NOT NULL,
    "language" varchar   NOT NULL,
    CONSTRAINT "pk_OMDB_language" PRIMARY KEY (
        "language_no"
     )
);

CREATE TABLE "OMDB_title_language" (
    "language_no" int   NOT NULL,
    "show_id" int   NOT NULL,
    CONSTRAINT "pk_OMDB_title_language" PRIMARY KEY (
        "language_no","show_id"
     )
);

CREATE TABLE "cast" (
    "cast_no" int   NOT NULL,
    "cast" varchar   NOT NULL,
    CONSTRAINT "pk_cast" PRIMARY KEY (
        "cast_no"
     )
);

CREATE TABLE "title_cast" (
    "cast_no" int   NOT NULL,
    "show_id" int   NOT NULL,
    CONSTRAINT "pk_title_cast" PRIMARY KEY (
        "cast_no","show_id"
     )
);

ALTER TABLE "OMDB_title_genre" ADD CONSTRAINT "fk_OMDB_title_genre_omdb_genre_no" FOREIGN KEY("omdb_genre_no")
REFERENCES "OMDB_genre" ("omdb_genre_no");

ALTER TABLE "OMDB_title_genre" ADD CONSTRAINT "fk_OMDB_title_genre_show_id" FOREIGN KEY("show_id")
REFERENCES "Title" ("show_id");

ALTER TABLE "Netflix_title_Listed_in" ADD CONSTRAINT "fk_Netflix_title_Listed_in_netflix_genre_no" FOREIGN KEY("netflix_genre_no")
REFERENCES "Netflix_Listed_in" ("netflix_genre_no");

ALTER TABLE "Netflix_title_Listed_in" ADD CONSTRAINT "fk_Netflix_title_Listed_in_show_id" FOREIGN KEY("show_id")
REFERENCES "Title" ("show_id");

ALTER TABLE "OMDB_title_language" ADD CONSTRAINT "fk_OMDB_title_language_language_no" FOREIGN KEY("language_no")
REFERENCES "OMDB_language" ("language_no");

ALTER TABLE "OMDB_title_language" ADD CONSTRAINT "fk_OMDB_title_language_show_id" FOREIGN KEY("show_id")
REFERENCES "Title" ("show_id");

ALTER TABLE "title_cast" ADD CONSTRAINT "fk_title_cast_cast_no" FOREIGN KEY("cast_no")
REFERENCES "cast" ("cast_no");

ALTER TABLE "title_cast" ADD CONSTRAINT "fk_title_cast_show_id" FOREIGN KEY("show_id")
REFERENCES "Title" ("show_id");