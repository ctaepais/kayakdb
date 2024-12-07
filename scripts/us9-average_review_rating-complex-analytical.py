from common import *

def average_review_rating(providerID):
    
    us = '''
    US9: View Average Review Rating
    Type: Complex + Analytical

    As a:  Service Provider
    I want:  To view the average review rating of my services
    So That:  I can improve offerings to attract more customers
    
    Case: View the average review rating of Marriot
    Function Call: average_review_rating(4)
    '''
    
    print(us)
    
    cols = "name, type, reviewrating"
    
    query = '''
        SELECT s.name, s.type, ROUND(AVG(r.rating), 2)
          FROM Service_Provider AS s 
               JOIN Travel_Service AS t ON s.providerid = t.providerid
               JOIN Review AS r ON t.listingid = r.listingid
         WHERE s.providerid = %s
         GROUP BY s.name, s.type
    '''
    
    cmd = cur.mogrify(query, (providerID,))
    cur.execute(cmd)
    rows = cur.fetchall()
    print("Average Review Rating")
    show_table(rows, cols)
    
    return

average_review_rating(4)