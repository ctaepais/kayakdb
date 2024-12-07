from common import *

def write_review(userID, listingID, rating, comment):
    
    us = '''
    US3: Update Review Rating
    Type: Complex + Operational
    
    As a: Administrator
    I want: Automatically update service and provider ratings when reviews are made or deleted
    So that: Users always see accurate review ratings for services
    
    Case: Update review rating of travel service and provider when a 5 star review is written for listingID 1 by userID 1
    Function Call: write_review(1, 1, 5, "Awesome Sauce")
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
    
write_review(1, 1, 5, "Awesome Sauce")
    