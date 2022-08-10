-- Create db 'hbtn_0d_usa'
-- If db already exists, script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
 
-- Create table 'cites' in db 'hbtn_0d_usa'
-- id INT unique auto-generated not null and primary key
-- state_id as a foreign key
-- name VARCHAR(256) not null
-- If table already exists, script should not fail
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities
(id INT UNIQUE AUTO_INCREMENT NOT NULL,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
PRIMARY KEY(id),
FOREIGN KEY(state_id)
	REFERENCES hbtn_0d_usa.states(id)
);
