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
                                        database="psz_realestate")

            cursor=connection.cursor()

            # A)
            for_sale_query='select * from "realty";'
            cursor.execute(for_sale_query)
            with open("analysis/database.csv", "w", newline='') as csv_file:
                csv_writer=csv.writer(csv_file)
                csv_writer.writerow([i[0] for i in cursor.description])  # write headers
                csv_writer.writerows(cursor)


        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: ", error)
        finally:
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()

    analyze()
