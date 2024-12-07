from common import*

def filter_date(startDate, endDate):
    
    us='''
    * US4: Filter Date
    Type: Simple + Operational
    As a:  Traveler
    I want:  To filter search results for a rental car by a date range
    So That:  I can find car options available when I need them

    '''

    print(us)
    
    # for the sake of data availability, I am just using all locations
    # the US does not explicitly state if its for a specific trip - so this is just all available cars

    cols = 'brand, modelName, rentalCompany, modelYear, startDate, endDate, price, reviewRating'
    
    table = '''
        SELECT r.brand, r.modelName, r.rentalCompany, r.modelYear, t.startDate, t.endDate, t.price, t.reviewRating
          FROM Rental_Car r
          JOIN Travel_Service t ON r.listingID = t.listingID
          JOIN Service_Provider s ON t.providerID = s.providerID
         WHERE t.startDate >= %s AND t.startDate <= %s
                AND t.available = TRUE
                AND s.currentPartner = TRUE
    '''
    print("Showing rental cars available starting from: ", startDate, " to ", endDate)
    print()

    # print matching table
    cmd = cur.mogrify(table, (startDate, endDate,))
    cur.execute(cmd)
    rows = cur.fetchall()
    print("Travel Services")
    show_table(rows, cols)

filter_date('2024-12-22', '2025-01-05')