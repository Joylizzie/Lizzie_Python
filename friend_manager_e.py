import psycopg2
import datetime

try:
    connection = psycopg2.connect(user="postgres",
                              password="Dan",
                              host="localhost",
                              port="5432",
                              database="friend_manager")
    cursor = connection.cursor()
    print(connection.get_dsn_parameters(),"\n")
    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

    def insert_person_list(cur):
        sql = '''insert into persons(name, date_of_birth) values
        ('Iris', '1975-10-09'),
        ('Vivi','1989-12-10');
        '''
        cur.execute(sql)

    insert_person_list(cursor)
    connection.commit()

    sql = '''
    select name,count(*)
    from persons
    group by name
    having count(*) > 1;'''
    cursor.execute(sql)
    duplicate_person_records = cursor.fetchall()
    print(duplicate_person_records)

    sql = '''
    delete persons 
    (select * from
    (select *,count(*)
    over
    (PARTITION BY name) as count
    from persons) tableWithCount
    where tableWithCount.count > 1;'''

    cursor.execute(sql)


   # sql = '''WITH unique AS
   #(select distinct on * from persons)
   #delete from persons where persons.id NOT IN(Select id from unique);'''
    cursor.execute(sql)
    connection.commit()

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    # closing database connection.
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")