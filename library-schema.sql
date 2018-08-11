-- sqlite3 library.db < library-schema.sql

drop table if exists country;
create table country (
    id integer primary key autoincrement,
    name text not null
);

drop table if exists person;
create table person (
    id integer primary key autoincrement,
    country_id integer,
    name text not null   
);

drop table if exists work;
create table work (
    id integer primary key autoincrement,
    person_id integer,
    achievement text not null,
    years integer
);