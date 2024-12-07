from common import *

def filter_car_preferences(userID):
    
    us = '''
    US7: Filter Car Preferences
    Type: Complex + Operational
    
    As a: Traveler
    I want: To filter car results by saved brand and home city preferences  
    So that: I can only see travel options that suit my selected preferences and save time
    
    Case: Filter Bob's search for rental cars: Ford in Los Angeles
    Function Call: filter_car_preferences(3)
    '''
    
    print(us)
    
    user_check_query = '''
        SELECT name, homecity, preferredcarbrand
          FROM Registered_User
         WHERE userid = %s
    '''
    cmd = cur.mogrify(user_check_query, (userID,))
    cur.execute(cmd)
    userpref = cur.fetchall()

    if not userpref:
        print("Invalid user ID.")
        return
    
    cols = "name, homecity, preferredcarbrand"
    print("User Car Preferences")
    show_table(userpref, cols)

    rental_query = '''
        SELECT c.brand, c.modelname, t.startdate, t.enddate, t.price, c.rentalcompany, c.pickuplocation
          FROM Rental_Car AS c
               JOIN Travel_Service AS t ON c.listingid = t.listingid
               JOIN Service_Provider AS s ON t.providerid = s.providerid
         WHERE c.pickuplocation LIKE CONCAT('%%',%s,'%%')
               AND c.brand = %s
               AND t.startdate >= current_date
               AND t.available = TRUE
               AND s.currentpartner = TRUE
         ORDER BY startdate ASC
    '''
    cmd = cur.mogrify(rental_query, (userpref[0][1], userpref[0][2],))
    cur.execute(cmd)
    rows = cur.fetchall()

    if not rows:
        print("No rental cars match the preferences.")
        return

    cols = 'brand, modelname, startdate, enddate, price, rentalcompany, pickuplocation'
    print("Rental Cars Filtered")
    show_table(rows, cols)

filter_car_preferences(3)