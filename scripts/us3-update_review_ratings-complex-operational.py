from common import *

def write_review(userID, listingID, rating, comment):
    
    us = '''
    US3: Set Price Alert
    Type: Complex + Operational
    
    As a: Traveler
    I want: Set a price alert for flights
    So that: I am notified when the fare drops to my desired price
    
    Case: Send a notification once the price of flight with listingID 4 drops below $1000
    Function Call: filter_car_preferences(4, 1000)
    '''
    
    listingrating = '''
        SELECT listingid, reviewrating
          FROM Travel_Service
         WHERE listingid = %s
    '''
    
    serviceproviderrating = '''
        SELECT s.name, s.reviewrating
          FROM Service_Provider s
               JOIN Travel_Service t ON s.providerid = t.providerid
         WHERE t.listingid = %s
    '''
    
    cmd = cur.mogrify(listingrating, (listingID,))
    cur.execute(cmd)
    listing = cur.fetchall()
    
    cmd = cur.mogrify(serviceproviderrating, (listingID,))
    cur.execute(cmd)
    serviceprovider = cur.fetchall()
    
    print("Before New Review:")
    show_table(listing, "listingid, reviewrating")
    show_table(serviceprovider, "name, reviewrating")
    
    insert_query = '''
        INSERT INTO Review (reviewid, postdate, rating, comment, listingid, userid)
        VALUES (
            (SELECT MAX(reviewID) + 1 FROM REVIEW),
            CURRENT_DATE,
            %s,
            %s,
            %s,
            %s
        )
    '''
    
    cmd = cur.mogrify(insert_query, (rating, comment, listingID, userID,))
    cur.execute(cmd)
    
    cmd = cur.mogrify(listingrating, (listingID,))
    cur.execute(cmd)
    listing = cur.fetchall()
    
    cmd = cur.mogrify(serviceproviderrating, (listingID,))
    cur.execute(cmd)
    serviceprovider = cur.fetchall()
    
    print("After New Review:")
    show_table(listing, "listingid, reviewrating")
    show_table(serviceprovider, "name, reviewrating")
    
    return
    
write_review(1, 1, 5, "Test Review")
    