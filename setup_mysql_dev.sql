-- Check if database hbnb_dev_db exists, if not, create it  
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;  

-- Check if user hbnb_dev exists, if not, create it  
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';  

-- Grant all privileges on hbnb_dev_db to hbnb_dev user  
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';  

-- Grant SELECT privilege on performance_schema to hbnb_dev user  
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';  

-- Flush privileges to ensure that changes take effect  
FLUSH PRIVILEGES;
