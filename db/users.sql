CREATE TABLE users (
    userId serial primary key,
    name varchar(55),
    email varchar(255),
    email_confirm BOOLEAN NOT NULL,
    password varchar(255)
);
