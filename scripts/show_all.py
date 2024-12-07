from common import *

def print_table(table_name):
    
    table = table_name.lower()
    
    querycols = '''
        SELECT COLUMN_NAME
          FROM INFORMATION_SCHEMA.COLUMNS
         WHERE TABLE_SCHEMA = 'public' AND TABLE_NAME = %s
         ORDER BY ORDINAL_POSITION
    '''
    
    cmd = cur.mogrify(querycols, (table,))
    cur.execute(cmd)
    cols = ' '.join(col[0] for col in cur.fetchall())
    
    query = '''
        SELECT *
          FROM {}
         LIMIT 10
    '''.format(table)

    # limiting to 10 here since we have a lot of example data that was needed, but would be too much to print

    cmd = cur.mogrify(query, (table,))
    cur.execute(cmd)
    rows = cur.fetchall()
    print(table_name)
    show_table( rows, cols) 
    print("\n")

tables = ['Users', 'Registered_User', 'Guest_User', 'Searches', 'Service_Provider', 'Travel_Service', 'Aircraft', 'Flight2', 'Flight1', 'Hotel_Room', 'Rental_Car', 'Returns', 'Review']

for table_name in tables:
    print_table(table_name)