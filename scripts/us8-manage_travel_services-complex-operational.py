from common import *

def update_service_availability(status, id):
    
    us='''
    US8: Manage Travel Services
    Type: Complex + Operational

    As a:  Service Provider
    I want:  To update and change the available inventory of services
    So That:  The platform reflects the current service status and availability
    
    Case: Update travel service (id = 1) to be unavailable (available = False)
    Function Call: update_service_availability(False, 1)
    '''

    print(us)
    
    cols = 'listingID, available'
    
    table = '''
        SELECT listingID, available
          FROM Travel_Service
         WHERE listingID = %s
    '''
    
    # print original table
    cmd = cur.mogrify(table, (id,))
    cur.execute(cmd)
    rows = cur.fetchall()
    print("Travel Service")
    show_table(rows, cols) 
    
    query = f'''
        UPDATE Travel_Service
           SET available = %s
         WHERE listingID = %s
    '''
    
    # update availability
    cmd = cur.mogrify(query, (status, id,))
    cur.execute(cmd)
    
    # print new table
    cmd = cur.mogrify(table, (id,))
    cur.execute(cmd)
    rows = cur.fetchall()
    print("Updated Travel Service")
    show_table(rows, cols) 

update_service_availability(False, 1)