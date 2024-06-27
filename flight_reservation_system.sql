CREATE DATABASE flight_reservation_systems;

USE flight_reservation_system;

CREATE TABLE flightss (
    flight_id INT AUTO_INCREMENT PRIMARY KEY,
    flight_name VARCHAR(100) NOT NULL,
    origin VARCHAR(100) NOT NULL,
    destination VARCHAR(100) NOT NULL,
    departure_date DATE NOT NULL,
    capacity INT NOT NULL
);

CREATE TABLE passengers (
    passenger_id INT,
    name VARCHAR(100) NOT NULL PRIMARY KEY,
    age INT NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    flight_id INT,
    FOREIGN KEY (flight_id) REFERENCES flights(flight_id)
);
CREATE TABLE airports (
    airport_id INT AUTO_INCREMENT PRIMARY KEY,
    airport_name VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL
);
INSERT INTO flightss (flight_name, origin, destination, departure_date, capacity)
VALUES
    ('Flight 1', 'New Delhi', 'Mumbai', '2024-07-01', 150),
    ('Flight 2', 'Bangalore', 'Chennai', '2024-07-02', 120),
    ('Flight 3', 'Kolkata', 'Hyderabad', '2024-07-03', 100),
    ('Flight 4', 'Pune', 'Jaipur', '2024-07-04', 110);
INSERT INTO passengers (passenger_id,name, age, gender, flight_id)
VALUES
    (1,'John Doe', 30, 'Male', 1),
    (2,'Jane Smith', 25, 'Female', 2),
    (3,'Michael Brown', 40, 'Male', 3),
    (4,'Emily Davis', 35, 'Female', 4),
    (5,'David Miller', 28, 'Male', 5);
INSERT INTO airports (airport_name, city, country)
VALUES
    ('Indira Gandhi International Airport', 'New Delhi', 'India'),
    ('Chhatrapati Shivaji Maharaj International Airport', 'Mumbai', 'India'),
    ('Kempegowda International Airport', 'Bangalore', 'India'),
    ('Chennai International Airport', 'Chennai', 'India'),
    ('Netaji Subhas Chandra Bose International Airport', 'Kolkata', 'India'),
    ('Rajiv Gandhi International Airport', 'Hyderabad', 'India'),
    ('Pune Airport', 'Pune', 'India'),
    ('Jaipur International Airport', 'Jaipur', 'India');
select * from passengers;
drop TABLE flightss;
drop TABLE passengers;
drop TABLE airports;
drop DATABASE flight_reservation_systems;
