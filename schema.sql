CREATE TABLE IF NOT EXISTS employees (
	employee_id serial PRIMARY KEY,
	first_name VARCHAR (255),
	last_name VARCHAR (355),
	birth_date DATE NOT NULL,
	hire_date DATE NOT NULL
);


CREATE TABLE IF NOT EXISTS tt (
	id serial PRIMARY KEY,
	name VARCHAR (255)
);

