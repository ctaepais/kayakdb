from common import *

def provider_rating(providerID):
    
    service_ratings = '''
        SELECT t.listingid, t.providerid, AVG(r.reviewrating)
          FROM Travel_Service t JOIN Review r ON t.listingid = r.listingid
         WHERE t.providerid = %s
         GROUP BY t.listingid, t.providerid
    '''
    
    cmd = cur.mogrify(service_ratings, (providerID,))
    rows = cur.fetchall()
    show_table(rows, "listingid, providerid, reviewrating")

provider_rating(4)