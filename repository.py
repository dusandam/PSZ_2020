import psycopg2


class Repository:

    def insert_data(self, data):
        connection = None
        try:
            connection=psycopg2.connect(user="dusandam",
                                        password="dusandam",
                                        host="localhost",
                                        port="5432",
                                        database="psz_realestate")

            cursor=connection.cursor()
            print(data)
            insert_into_query='INSERT INTO "realty"(' \
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
                              'price,' \
                              'city,'\
                              'quarter,' \
                              'webpage)' \
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