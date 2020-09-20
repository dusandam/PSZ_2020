import psycopg2
import csv


class Analysis:

    def analyze():
        connection=None
        try:
            connection=psycopg2.connect(user="dusandam",
                                        password="dusandam",
                                        host="localhost",
                                        port="5432",
                                        database="nekretnine")

            cursor=connection.cursor()

            # A)
            for_sale_query='delete from "Realty" where year_built > 2020;'
            cursor.execute(for_sale_query)
            connection.commit()

            for_sale_query='delete from "Realty" where year_built < 1600;'
            cursor.execute(for_sale_query)
            connection.commit()


        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: ", error)
        finally:
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()

    analyze()
