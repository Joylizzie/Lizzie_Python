import psycopg2
from psycopg2 import Error

def connect()
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Dan",
                                      host="localhost",
                                      port="5432",
                                      database="friend_manager")

        connection.autocommit = False
        cursor = connection.cursor()

        print(connection.get_dsn_parameters(), "\n")

        cursor.execute("""select version();""")
        record = cursor.fetchone()
        print("You are connected to ", record, "\n")

        sql1 = '''update persons
                set date_of_birth = '1997-09-08'
                where name = 'Lisa Scott'
                and date_of_birth = '1999-11-25'
                '''

        sql2 = '''insert into persons(name, date_of_birth) values
                ('Vivi', '2000-04-06'),
                ('Susan','1985-05-30');
                '''

        sql3 = '''delete from persons
                    where id in
                        (
                            select id from 
                                    (select id,
                                            row_number() OVER (PARTITION BY(name,date_of_birth) order by id) as row_num
                                    from persons) as t
                            where row_num > 1
                        )
                '''

        cursor.execute(sql1)
        cursor.execute(sql2)
        cursor.execute(sql3)

        connection.commit

        cursor.execute("select * from persons;")
        record = cursor.fetchall()
        print("This is your new friend list records: ", record, '\n')


    except(Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("Postgresql connection is closed")



if __name__ == '__main__':
    connect()

