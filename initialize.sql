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

-- Functions

-- Calculate and update provider rating
CREATE OR REPLACE FUNCTION update_ratings()
RETURNS trigger
LANGUAGE plpgsql AS
$$
DECLARE
    listing_id INT;
BEGIN
    -- check operation
    IF (TG_OP = 'DELETE') THEN
        listing_id = OLD.listingid;
    ELSE
        listing_id = NEW.listingid;
    END IF;

    -- update rating of travel service
    UPDATE Travel_Service
       SET reviewrating = (
           SELECT ROUND(AVG(rating), 2)
             FROM Review
            WHERE listingid = listing_id
       )
     WHERE listingid = listing_id

    -- update rating of service provider
    UPDATE Service_Provider
       SET reviewRating = (
           SELECT ROUND(AVG(r.rating), 2)
             FROM Review r
                  JOIN Travel_Service t ON r.listingid = t.listingid
            WHERE listingid = listing_id
       )
      WHERE providerid = (
        SELECT providerid
          FROM Travel_Service
         WHERE listingid = listing_id
      )
      RETURN NEW;
END
$$;

-- Trigger to update provider rating upon new/updated/deleted review
CREATE TRIGGER new_review_rating_trigger
AFTER INSERT OR UPDATE OR DELETE ON Review
FOR EACH ROW
EXECUTE FUNCTION update_ratings();
