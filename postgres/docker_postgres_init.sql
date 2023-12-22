-- Create the database
CREATE DATABASE demo1
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

-- Connect to the demo1 database
\c demo1

-- Create tables
CREATE TABLE Department (
  department_name VARCHAR(255) PRIMARY KEY
);

CREATE TABLE Sensor (
  sensor_serial VARCHAR(255) PRIMARY KEY,
  department_name VARCHAR(255) NOT NULL REFERENCES Department(department_name)
);

CREATE TABLE Product (
  product_id SERIAL PRIMARY KEY,
  product_name VARCHAR(255) NOT NULL,
  sensor_serial VARCHAR(255) NOT NULL REFERENCES Sensor(sensor_serial),
  create_at TIMESTAMP
);

CREATE TABLE ProductExpiry (
  product_expiry_id SERIAL PRIMARY KEY,
  product_id INT NOT NULL REFERENCES Product(product_id),
  expiry_date TIMESTAMP,
  create_at TIMESTAMP
);
