from common import *

def monitor_searches(start_date, end_date):
    
    us = '''
    US5: Monitor Searches
    Type: Complex + Analytical
    
    As an: Administrator
    I want: Track and rank the most searched travel services during a certain travel season
    So that: I can identify high-demand destinations and improve suggestions
    
    Case: Find the most searched for travel services during the holiday season
    Function Call: monitor_searches(1)
    '''

    print(us)

    cols = '''listingID destinationLocation name type startDate searchCount rank'''

    search_query = '''
        SELECT r.listingID, t.destinationLocation, p.name, p.type, t.startDate, 
               count(s.searchID) as searchCount, DENSE_RANK() OVER W as rank
          FROM Searches AS s
               JOIN Returns AS r ON s.searchID = r.searchID
               JOIN Travel_Service AS t ON r.listingID = t.listingID
               JOIN Service_Provider AS p ON t.providerID = p.providerID
         WHERE s.timestamp >= %s AND s.timestamp <= %s
         GROUP BY r.listingID, t.destinationLocation, p.name, p.type, t.startDate
        WINDOW W AS (ORDER BY count(s.searchID) DESC)
        ORDER BY rank, t.destinationLocation DESC, r.listingID


    '''


    
    # print new table
    cmd = cur.mogrify(search_query, (start_date, end_date,))
    cur.execute(cmd)
    rows = cur.fetchall()
    print("Serivce Providers")
    show_table(rows, cols) 



monitor_searches('2024-11-1', '2025-01-01')