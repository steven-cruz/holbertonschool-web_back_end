-- SQL script that create a table users
-- script can be executed on any database
CREATE TABLE IF NOT EXISTS users (
       id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
       email VARCHAR(255) NOT NULL UNIQUE,
       name VARCHAR(255)
);
