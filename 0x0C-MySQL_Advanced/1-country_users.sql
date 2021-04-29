-- Create a table users
-- If the table exists, your script should not fail
CREATE TABLE IF NOT EXISTS users(
       id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
       imail VARCHAR(255) NOT NULL UNIQUE,
       name VARCHAR(255),
       country ENUM('US', 'CO', 'TN') NOT NULL
);
