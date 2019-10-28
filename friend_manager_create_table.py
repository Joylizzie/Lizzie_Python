import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user = 'postgres',
                                  password = 'Dan',
                                  host = '127.0.0.1',
                                  port = '5432',
                                  database = 'friend_manager')

    cursor = connection.cursor()

    cursor.execute("drop table if exists address_1")

    create_table = '''CREATE table address_1
    (friend_id int primary key not null,
    house_number varchar(20),
    street_name varchar(50),
    city varchar(20),
    state varchar(20),
    country varchar(20),
    primary_address boolean);
    '''
    cursor.execute(create_table)
    connection.commit()
    print("Table created successfully in PostgreSQL ")

except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while creating PostgreSQL table", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")