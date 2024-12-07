from common import*

def manage_providers(providerID):
    
    us='''
    * US6: 
    Type: Simple + Operational

    As a:  Administrator
    I want:  To change the partnered status of service providers
    So That:  The platform reflects the current status of service providers

    '''
    
    print(us)
    
    cols = 'providerID, name, type, currentPartner'
    
    table = '''
        SELECT providerID, name, type, currentPartner
        FROM Service_Provider
        ORDER BY providerID
    '''

    # print original table
    cmd = cur.mogrify(table)
    cur.execute(cmd)
    rows = cur.fetchall()

    print("Initial Service Provider Table") 
    show_table(rows, cols) 
    
    print("Setting provider with id:", providerID, "to have the opposite currentPartner status")
    print()

    # Remove non partnered service providers from table
    # this query just flips the currentPartner status, so if it was true, it will be false and vice versa
    
    query = '''
        UPDATE Service_Provider
        SET currentPartner = NOT currentPartner
        WHERE providerID = %s
    '''
    cmd = cur.mogrify(query, (providerID,))
    cur.execute(cmd)

    
    # print new table
    cmd = cur.mogrify(table)
    cur.execute(cmd)
    rows = cur.fetchall()
    # pp(rows)
    print("Serivce Providers")
    show_table(rows, cols) 
        
manage_providers(9)