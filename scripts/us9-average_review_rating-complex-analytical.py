from common import *

def total_travel_services(providerID):
    
    us = '''
    US9: View Total Available Service Listings
    Type: Complex + Analytical

    As a:  Service Provider
    I want:  To view the total number of available travel service listings
    So That:  I can manage offerings to attract more customers
    
    Case: View the total number of available travel listings of Marriot
    Function Call: total_travel_services(4)
    '''
    
    print(us)
    
    cols = "name, type, totallistings"
    
    query = '''
        SELECT s.name, s.type, COUNT(listingid)
          FROM Service_Provider AS s 
               JOIN Travel_Service AS t ON s.providerid = t.providerid
         WHERE s.providerid = %s AND t.available = TRUE
         GROUP BY s.name, s.type
    '''
    
    cmd = cur.mogrify(query, (providerID,))
    cur.execute(cmd)
    rows = cur.fetchall()
    print("Total Travel Listings")
    show_table(rows, cols)
    
    return

total_travel_services(4)