from common import*

def create_profile(userID, email, phoneNumber, password, name, homeCity, preferredAirline, preferredClass, preferredCarBrand):
    
    us='''
    * US1: Create Profile
    Type: Simple + Operational

    As a:  Traveler
    I want:  To create a profile
    So That:  I can save personal information, travel preferences, and bookmarked services

    Case: Create a new profile for Edward
    Function Call: create_profile(21, "user11@gmail.com", 1234567999, "pass11", "Edward", "Pittsburgh", "Jet Blue", "Economy", "Toyota")
    '''
    
    print(us)
    
    cols = 'userID email phoneNumber password name homeCity preferredAirline preferredClass preferredCarBrand'
    
    table = '''
        SELECT *
        FROM Registered_User
    '''

    # print original table
    cmd = cur.mogrify(table)
    cur.execute(cmd)
    rows = cur.fetchall()
    # pp(rows)
    print("Registered User Table Initial") 
    show_table(rows, cols) 
    
    print("Inserting new user to Users table, UserID: ", userID)
    print()

    # Insert into User table first
    user_query = '''
        INSERT INTO Users(userID)
        VALUES(%s)
    '''
    cmd = cur.mogrify(user_query, (userID,))
    cur.execute(cmd)

    # Insert into Registered_User table

    query = f'''
        INSERT INTO Registered_User(userID, email, phoneNumber, password, name, homeCity, preferredAirline, preferredClass, preferredCarBrand)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''
    
    # Insert new user
    print("Inserting new user to Registered_User table: ","[", userID,",", email,",", phoneNumber,",", password,",", name,",", homeCity,",", preferredAirline,",", preferredClass,",", preferredCarBrand,"]")
    print()
    cmd = cur.mogrify(query, (userID, email, phoneNumber, password, name, homeCity, preferredAirline, preferredClass, preferredCarBrand))
    cur.execute(cmd)
    
    # print new table
    cmd = cur.mogrify(table)
    cur.execute(cmd)
    rows = cur.fetchall()
    # pp(rows)
    print("Registered User")
    show_table(rows, cols) 
        
create_profile(21, "user11@gmail.com", 1234567999, "pass11", "Edward", "Pittsburgh", "Jet Blue", "Economy", "Toyota")