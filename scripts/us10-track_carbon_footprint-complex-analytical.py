from common import *

def total_carbon_footprint(providerID, year):
    
    us = '''
    US10: Track Carbon Footprint
    Type: Complex + Analytical

    As a:  Service Provider
    I want:  To view the total carbon emissions of travel services in a certain year
    So That:  I can report my services' environmental impact to stakeholders
    
    Case: View the total carbon footprint of American Airlines in 2024
    Function Call: total_carbon_footprint(8, 2024)
    '''
    
    print(us)
    
    cols = "name, type, carbonfootprint"
    
    query = '''
        SELECT s.name, s.type, SUM(t.carbonfootprint)
          FROM Service_Provider AS s 
          JOIN Travel_Service AS t ON s.providerid = t.providerid
         WHERE s.providerid = %s AND EXTRACT(YEAR FROM t.startdate) = %s
         GROUP BY s.name, s.type
    '''
    
    cmd = cur.mogrify(query, (providerID, year))
    cur.execute(cmd)
    rows = cur.fetchall()
    print("Carbon Emissions")
    show_table( rows, cols) 
    
    return

total_carbon_footprint(8, 2024)