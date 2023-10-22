CREATE TABLE steps (
    stepid serial PRIMARY KEY,
    userId int references users(userId),
    step_date date,
    step_count int,
    step_count_target BOOLEAN NOT NULL
);