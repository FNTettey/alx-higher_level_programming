-- Creating a database if it doesn't exist
-- If the database hbtn_0d_2 already exists, your script should not 
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- creating a new user user_0d_2
-- password should be set to user_0d_2_pwd
-- If the user user_0d_2 already exists, your script should not fail
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';

-- User 'user_0d_2' should have only SELECT privilege in db 'hbtn_0d_2'
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
