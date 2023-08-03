-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	employee_id serial PRIMARY KEY,
	first_name varchar(15) NOT NULL,
	last_name varchar(15) NOT NULL,
	title varchar(30) NOT NULL,
	birth_date date,
	notes text
);
CREATE TABLE customers
(
	customer_id varchar(5) PRIMARY KEY,
	company_name varchar(40) NOT NULL,
	contact_name varchar(40) NOT NULL
);
CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer varchar(5) NOT NULL,
	employee int NOT NULL,
	order_date date NOT NULL,
	ship_sity varchar(20) NOT NULL,
	FOREIGN KEY (customer) REFERENCES customers(customer_id),
    FOREIGN KEY (employee) REFERENCES employees(employee_id)
);