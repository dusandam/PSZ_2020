import psycopg2


class Repository:

    def insert_data(self):
        connection = None
        try:
            connection=psycopg2.connect(user="dusandam",
                                        password="dusandam",
                                        host="localhost",
                                        port="5432",
                                        database="psz_realestate")

            cursor=connection.cursor()

            insert_into_query='select count(*) from "realty"'

            cursor.execute(insert_into_query)
            print(cursor.fetchall())
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error importing data", error)
        finally:
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()

    def empty_database(self):
        connection = None
        try:
            connection=psycopg2.connect(user="dusandam",
                                        password="dusandam",
                                        host="localhost",
                                        port="5432",
                                        database="psz_realestate")

            cursor=connection.cursor()

            clean_database='delete from "realty"'
            cursor.execute(clean_database)
            connection.commit()
            print("Database_empty: ")

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error emptying database", error)
        finally:
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()

    insert_data(None)