-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2024-12-07 22:55:48.585

-- tables
-- Table: Aircraft
CREATE TABLE Aircraft (
    aircraftID int  NOT NULL,
    model text  NOT NULL,
    age int  NOT NULL,
    seatingCapacity int  NOT NULL,
    amenities text  NOT NULL,
    entertainmentSystems text  NOT NULL,
    CONSTRAINT Aircraft_pk PRIMARY KEY (aircraftID)
);

-- Table: Flight1
CREATE TABLE Flight1 (
    listingID int  NOT NULL,
    flightNumber text  NOT NULL,
    departureTime time  NOT NULL,
    arrivalTime time  NOT NULL,
    departureAirport text  NOT NULL,
    arrivalAirport text  NOT NULL,
    aircraftID int  NOT NULL,
    CONSTRAINT Flight1_pk PRIMARY KEY (listingID)
);

-- Table: Flight2
CREATE TABLE Flight2 (
    flightNumber text  NOT NULL,
    airline text  NOT NULL,
    CONSTRAINT Flight2_pk PRIMARY KEY (flightNumber)
);

-- Table: Guest_User
CREATE TABLE Guest_User (
    userID int  NOT NULL,
    IPAddress text  NOT NULL,
    timestamp timestamp  NOT NULL,
    CONSTRAINT Guest_User_pk PRIMARY KEY (userID)
);

-- Table: Hotel_Room
CREATE TABLE Hotel_Room (
    listingID int  NOT NULL,
    name text  NOT NULL,
    address text  NOT NULL,
    roomType text  NOT NULL,
    beds int  NOT NULL,
    CONSTRAINT Hotel_Room_pk PRIMARY KEY (listingID)
);

-- Table: Registered_User
CREATE TABLE Registered_User (
    userID int  NOT NULL,
    email text  NOT NULL,
    phoneNumber int  NOT NULL,
    password text  NOT NULL,
    name text  NOT NULL,
    homeCity text  NOT NULL,
    preferredAirline text  NOT NULL,
    preferredClass text  NOT NULL,
    preferredCarBrand text  NOT NULL,
    CONSTRAINT Registered_User_pk PRIMARY KEY (userID)
);

-- Table: Rental_Car
CREATE TABLE Rental_Car (
    listingID int  NOT NULL,
    brand text  NOT NULL,
    modelName text  NOT NULL,
    rentalCompany text  NOT NULL,
    modelYear int  NOT NULL,
    pickupLocation text  NOT NULL,
    CONSTRAINT Rental_Car_pk PRIMARY KEY (listingID)
);

-- Table: Returns
CREATE TABLE Returns (
    searchID int  NOT NULL,
    listingID int  NOT NULL,
    CONSTRAINT Returns_pk PRIMARY KEY (searchID,listingID)
);

-- Table: Review
CREATE TABLE Review (
    reviewID int  NOT NULL,
    postDate date  NOT NULL,
    rating int  NOT NULL,
    comment text  NOT NULL,
    listingID int  NOT NULL,
    userID int  NOT NULL,
    CONSTRAINT Review_pk PRIMARY KEY (reviewID)
);

-- Table: Searches
CREATE TABLE Searches (
    searchID int  NOT NULL,
    timestamp timestamp  NOT NULL,
    bookmarked boolean  NOT NULL,
    userID int  NOT NULL,
    CONSTRAINT Searches_pk PRIMARY KEY (searchID)
);

-- Table: Service_Provider
CREATE TABLE Service_Provider (
    providerID int  NOT NULL,
    name text  NOT NULL,
    type text  NOT NULL,
    contactInfo text  NOT NULL,
    currentPartner boolean  NOT NULL,
    reviewRating decimal(3,2)  NOT NULL,
    CONSTRAINT Service_Provider_pk PRIMARY KEY (providerID)
);

-- Table: Travel_Service
CREATE TABLE Travel_Service (
    listingID int  NOT NULL,
    price decimal(20,2)  NOT NULL,
    startDate date  NOT NULL,
    endDate date  NOT NULL,
    destinationLocation text  NOT NULL,
    carbonFootprint int  NOT NULL,
    available boolean  NOT NULL,
    reviewRating decimal(3,2)  NOT NULL,
    providerID int  NOT NULL,
    CONSTRAINT Travel_Service_pk PRIMARY KEY (listingID)
);

-- Table: Users
CREATE TABLE Users (
    userID int  NOT NULL,
    CONSTRAINT Users_pk PRIMARY KEY (userID)
);

-- foreign keys
-- Reference: Flight1_Flight2 (table: Flight1)
ALTER TABLE Flight1 ADD CONSTRAINT Flight1_Flight2
    FOREIGN KEY (flightNumber)
    REFERENCES Flight2 (flightNumber)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Flight_Aircraft (table: Flight1)
ALTER TABLE Flight1 ADD CONSTRAINT Flight_Aircraft
    FOREIGN KEY (aircraftID)
    REFERENCES Aircraft (aircraftID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Guest_User (table: Guest_User)
ALTER TABLE Guest_User ADD CONSTRAINT Guest_User
    FOREIGN KEY (userID)
    REFERENCES Users (userID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Registered_User (table: Registered_User)
ALTER TABLE Registered_User ADD CONSTRAINT Registered_User
    FOREIGN KEY (userID)
    REFERENCES Users (userID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Returns_Travel_Service (table: Returns)
ALTER TABLE Returns ADD CONSTRAINT Returns_Travel_Service
    FOREIGN KEY (listingID)
    REFERENCES Travel_Service (listingID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Review_Travel_Service (table: Review)
ALTER TABLE Review ADD CONSTRAINT Review_Travel_Service
    FOREIGN KEY (listingID)
    REFERENCES Travel_Service (listingID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Searches_Returns (table: Returns)
ALTER TABLE Returns ADD CONSTRAINT Searches_Returns
    FOREIGN KEY (searchID)
    REFERENCES Searches (searchID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Travel_Service_Flight (table: Flight1)
ALTER TABLE Flight1 ADD CONSTRAINT Travel_Service_Flight
    FOREIGN KEY (listingID)
    REFERENCES Travel_Service (listingID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Travel_Service_Hotel_Room (table: Hotel_Room)
ALTER TABLE Hotel_Room ADD CONSTRAINT Travel_Service_Hotel_Room
    FOREIGN KEY (listingID)
    REFERENCES Travel_Service (listingID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Travel_Service_Rental_Car (table: Rental_Car)
ALTER TABLE Rental_Car ADD CONSTRAINT Travel_Service_Rental_Car
    FOREIGN KEY (listingID)
    REFERENCES Travel_Service (listingID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Travel_Service_Service_Provider (table: Travel_Service)
ALTER TABLE Travel_Service ADD CONSTRAINT Travel_Service_Service_Provider
    FOREIGN KEY (providerID)
    REFERENCES Service_Provider (providerID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: User_Review (table: Review)
ALTER TABLE Review ADD CONSTRAINT User_Review
    FOREIGN KEY (userID)
    REFERENCES Users (userID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: User_Searches (table: Searches)
ALTER TABLE Searches ADD CONSTRAINT User_Searches
    FOREIGN KEY (userID)
    REFERENCES Users (userID)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

