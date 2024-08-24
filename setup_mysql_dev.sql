-- This SQL script creates the necessary tables for the AirBnB clone project  

-- Create a new database  
CREATE DATABASE IF NOT EXISTS airbnb_db;  

-- Use the newly created database  
USE airbnb_db;  

-- Create the states table  
CREATE TABLE IF NOT EXISTS states (  
    id INT AUTO_INCREMENT PRIMARY KEY,  
    name VARCHAR(255) NOT NULL,  
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  
);  

-- Create the cities table  
CREATE TABLE IF NOT EXISTS cities (  
    id INT AUTO_INCREMENT PRIMARY KEY,  
    state_id INT NOT NULL,  
    name VARCHAR(255) NOT NULL,  
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  
    FOREIGN KEY (state_id) REFERENCES states(id) ON DELETE CASCADE  
);
