CREATE TABLE "owners"
(
    "id" SERIAL PRIMARY KEY,
    first_name varchar(255) NOT NULL,
    last_name varchar(255) NOT NULL
)
CREATE TABLE "pets"
(
    "id" SERIAL PRIMARY KEY,
    name varchar(255) NOT NULL,
    breed varchar(255) NOT NULL,
    color varchar(255) NOT NULL,
    is_checked_in varchar(255) NOT NULL,
    owners_id int REFERENCES "owners"
)