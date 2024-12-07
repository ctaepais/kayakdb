-- terminal command
-- psql -U isdb -d postgres -f initialize.sql

-- drop the kayak database if it exists
DROP database if EXISTS kayak;

-- create it afresh
CREATE database kayak;
\c kayak

CREATE TYPE Service_Type AS ENUM('airline', 'rentalCar', 'hotel');

\i create.SQL

-- load the data

-- User Tables
\copy Users(userID) FROM data/user.csv header csv;
\copy Registered_User(userID, email, phoneNumber, password, name, homeCity, preferredAirline, preferredClass, preferredCarBrand) FROM data/registered_user.csv header csv;
\copy Guest_User(userID, IPAddress, timestamp) FROM data/guest_user.csv header csv;

-- Searches
\copy Searches(searchID, timestamp, bookmarked, userID) FROM data/searches.csv header csv;

-- Service Tables
\copy Service_Provider(providerID, name, type, contactInfo, currentPartner, reviewRating) FROM data/service_provider.csv header csv;
\copy Travel_Service(listingID, price, startDate, endDate, destinationLocation, carbonFootprint, available, reviewRating, providerID) FROM data/travel_service.csv header csv;

\copy Aircraft(aircraftID, model, age, seatingCapacity, amenities, entertainmentSystems) FROM data/aircraft.csv csv header;
\copy Flight2(flightNumber, airline) FROM data/flight2.csv header csv;
\copy Flight1(listingID, flightNumber, departureTime, arrivalTime, departureAirport, arrivalAirport, aircraftID) FROM data/flight1.csv csv header;

\copy Hotel_Room(listingID, name, address, roomType, beds) FROM data/hotel_room.csv header csv;
\copy Rental_Car(listingID, brand, modelName, rentalCompany, modelYear, pickupLocation) FROM data/rental_car.csv header csv;

\copy Returns(searchID, listingID) FROM data/returns.csv header csv;
\copy Review(reviewID, postDate, rating, comment, listingID, userID) FROM data/review.csv header csv;