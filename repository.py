import psycopg2


class Repository:

    def insert_data(self, data):
        connection = None
        try:
            connection=psycopg2.connect(user="dusandam",
                                        password="dusandam",
                                        host="localhost",
                                        port="5432",
                                        database="nekretnine")

            cursor=connection.cursor()

            insert_into_query='INSERT INTO "Realty"(' \
                              'type,' \
                              'offer_type,' \
                              'square_meters,' \
                              'year_built,' \
                              'land_area,' \
                              'total_floors,' \
                              'floor,' \
                              'registered,' \
                              'heating_type,' \
                              'total_rooms,' \
                              'total_bathrooms,' \
                              'location_id,' \
                              'price,' \
                              'city,' \
                              'quarter)' \
                              'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

            cursor.execute(insert_into_query, data)
            connection.commit()
            # print("Data imported: ", data)

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
                                        database="nekretnine")

            cursor=connection.cursor()

            clean_database='delete from "Realty"'
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