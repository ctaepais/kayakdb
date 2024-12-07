from common import*

def sort_flights(departureAirport):
    
    us='''
    * US2: Sort Flights
    Type: Simple + Operational

    As a:  User
    I want:  To view flight options sorted by price
    So That:  I can find flights that fit my budget
    '''
    # for the sake of having data, I am just passsing the departureAirport as a parameter, and not dealing with dates & arrivals
    # the US does not explicitly state if its for a specific trip - so this is just flights from the selected airport by price

    print(us)
    
    cols = 'flightNumber, airline, departureTime, arrivalTime, departureAirport, arrivalAirport, price'
    
    table = '''
        SELECT f.flightNumber, f2.airline, f.departureTime, f.arrivalTime, f.departureAirport, f.arrivalAirport, t.price
          FROM Flight1 AS f
          JOIN Flight2 f2 ON f.flightNumber = f2.flightNumber
          JOIN Travel_Service t ON t.listingID = f.listingID
         WHERE f.departureAirport = %s
         ORDER BY price ASC
    '''
    print()
    print("Sorting Flights by Price From: ", departureAirport)
    print()
    # print sorted table
    cmd = cur.mogrify(table, (departureAirport,))
    cur.execute(cmd)
    rows = cur.fetchall()
    print("Flights")
    show_table(rows, cols)

sort_flights('DFW')