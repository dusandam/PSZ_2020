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
            for_sale_query='select count(*), offer_type from "Realty" group by offer_type;'
            cursor.execute(for_sale_query)
            with open("offer_count.csv", "w", newline='') as csv_file:
                csv_writer=csv.writer(csv_file)
                csv_writer.writerow([i[0] for i in cursor.description])  # write headers
                csv_writer.writerows(cursor)

            # B)
            listings_per_city='select city, count(realty_id) from "Realty" group by city order by city;'
            cursor.execute(listings_per_city)
            with open("listings_per_city.csv", "w", newline='') as csv_file:
                csv_writer=csv.writer(csv_file)
                csv_writer.writerow([i[0] for i in cursor.description])  # write headers
                csv_writer.writerows(cursor)

            # C)
            for_rent_query='select count(*), type from "Realty" where registered = ' + "true group by type;"
            cursor.execute(for_rent_query)
            with open("registered.csv", "w", newline='') as csv_file:
                csv_writer=csv.writer(csv_file)
                csv_writer.writerow([i[0] for i in cursor.description])  # write headers
                csv_writer.writerows(cursor)

            query='select count(*), type from "Realty" where registered is false group by type;'
            cursor.execute(query)
            with open("unregistered.csv", "w", newline='') as csv_file:
                csv_writer=csv.writer(csv_file)
                csv_writer.writerow([i[0] for i in cursor.description])  # write headers
                csv_writer.writerows(cursor)

            # D)
            query='select * from "Realty" where type like ' + "'kuca' and offer_type like 'prodaja' and price is not null order by price desc limit 20;"
            cursor.execute(query)
            with open("expensive_houses.csv", "w", newline='') as csv_file:
                csv_writer=csv.writer(csv_file)
                csv_writer.writerow([i[0] for i in cursor.description])  # write headers
                csv_writer.writerows(cursor)

            query='select * from "Realty" where type like ' + "'stan' and offer_type like 'prodaja' and price is not null order by price desc limit 20;"
            cursor.execute(query)
            with open("expensive_appartments.csv", "w", newline='') as csv_file:
                csv_writer=csv.writer(csv_file)
                csv_writer.writerow([i[0] for i in cursor.description])  # write headers
                csv_writer.writerows(cursor)

            # E)
            query='select * from "Realty" where type like ' + "'kuca' and offer_type like 'izdavanje' and price is not null order by price desc limit 100;"
            cursor.execute(query)
            with open("expensive_houses_rent.csv", "w", newline='') as csv_file:
                csv_writer=csv.writer(csv_file)
                csv_writer.writerow([i[0] for i in cursor.description])  # write headers
                csv_writer.writerows(cursor)


            query='select * from "Realty" where type like ' + "'stan' and offer_type like 'izdavanje' and price is not null order by price desc limit 100;"
            cursor.execute(query)
            with open("expensive_appartments_rent.csv", "w", newline='') as csv_file:
                csv_writer=csv.writer(csv_file)
                csv_writer.writerow([i[0] for i in cursor.description])  # write headers
                csv_writer.writerows(cursor)

            # F)
            query='select * from "Realty" where year_built = 2019 and price is not null order by price desc;'
            cursor.execute(query)
            with open("bulit_in_2019.csv", "w", newline='') as csv_file:
                csv_writer=csv.writer(csv_file)
                csv_writer.writerow([i[0] for i in cursor.description])  # write headers
                csv_writer.writerows(cursor)

            # G)
            query='select * from "Realty" r where total_rooms is not null and not exists (select * from "Realty" r2 where r2.total_rooms > r.total_rooms) order by price desc;'
            cursor.execute(query)
            with open("most_rooms.csv", "w", newline='') as csv_file:
                csv_writer=csv.writer(csv_file)
                csv_writer.writerow([i[0] for i in cursor.description])  # write headers
                csv_writer.writerows(cursor)


            query='select * from "Realty" r where total_bathrooms is not null and not exists (select * from "Realty" r2 where r2.total_bathrooms > r.total_bathrooms) order by price desc;'
            cursor.execute(query)
            with open("most_bathrooms.csv", "w", newline='') as csv_file:
                csv_writer=csv.writer(csv_file)
                csv_writer.writerow([i[0] for i in cursor.description])  # write headers
                csv_writer.writerows(cursor)


            query='select * from "Realty" r where land_area is not null and not exists (select * from "Realty" r2 where r2.land_area > r.land_area) order by price desc;'
            cursor.execute(query)
            with open("largest_land_area.csv", "w", newline='') as csv_file:
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
