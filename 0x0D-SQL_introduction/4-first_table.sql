#!/bin/bash/env mysql
-- Create first table in MySql
CREATE TABLE IF EXISTS first_table (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(256),
signup_date DATE);
