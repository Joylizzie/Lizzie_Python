import psycopg2
import datetime
import pdb


try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "Dan",
                                  host = "localhost",
                                  port = "5432",
                                  database = "friend_manager")
    connection.autocommit = False
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(),"\n")
    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

    dt = datetime.datetime.today()

    sql = '''
    select * from persons
    where extract(month from date_of_birth)::integer = %s
    and extract(day from date_of_birth)::integer = %s;
    '''

    cursor.execute(sql, (dt.month, dt.day))

    # cursor.execute("select *, extract(month from date_of_birth)::integer as month, extract(day from date_of_birth)::integer as day from persons;")
    #cursor.execute(query)
    person_records = cursor.fetchall()


    print(dt.year)
    print(dt.month)
    print(dt.day)

    for row in person_records:
        id = row[0]
        name = row[1]
        date_of_birth = row[2]
        #db_month = row[3]
        #db_day = row[4]
        print("Id = ", id, )
        print("name = ", name)
        print("date_of_birth  = ", date_of_birth)
        #print("db month = ", db_month)
        #print("db day = ", db_day, "\n")

        #if dt.month == db_month and dt.day == db_day:


        print("Today is the birthday of " + name)


except (Exception, psycopg2.Error) as error :
    print("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

