from common import *

def provider_rating(providerID):
    
    service_ratings = '''
        SELECT t.listingid, t.providerid, AVG(r.rating)
          FROM Travel_Service t JOIN Review r ON t.listingid = r.listingid
         WHERE t.providerid = %s
         GROUP BY t.listingid, t.providerid
         ORDER BY t.listingid
    '''
    
    cmd = cur.mogrify(service_ratings, (providerID,))
    cur.execute(cmd)
    rows = cur.fetchall()
    show_table(rows, "listingid, providerid, reviewrating")

provider_rating(4)