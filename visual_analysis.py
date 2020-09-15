import psycopg2
import csv
import subprocess
import sys

if sys.version_info[:2] < (3, 0):
    code=subprocess.call(['python3'] + sys.argv)
    raise SystemExit(code)

import matplotlib.pyplot as plt
import pandas as pd
import os

# ZADATAK 3, UPITI

class Visualize:

    def get_analysis():
        connection=None
        try:
            connection=psycopg2.connect(user="dusandam",
                                        password="dusandam",
                                        host="localhost",
                                        port="5432",
                                        database="nekretnine")

            cursor=connection.cursor()

            # A)
            query='select quarter, count(realty_id) from "Realty" where city like ' + "'Beograd' group by quarter order by count(realty_id) desc limit 8;"
            cursor.execute(query)
            with open("visualization/most_present_quarters.csv", "w", newline='') as csv_file:
                csv_writer=csv.writer(csv_file)
                csv_writer.writerow([i[0] for i in cursor.description])  # write headers
                csv_writer.writerows(cursor)

            # B)
            query='SELECT COUNT(CASE WHEN type like ' + "'stan'" + ' and square_meters is not null and square_meters <= 35 THEN 1 END) AS count1, ' \
                  'COUNT(CASE WHEN type like ' + "'stan'" + ' and square_meters is not null and square_meters between 36 and 50 THEN 1 END) AS count2, ' \
                  'COUNT(CASE WHEN type like ' + "'stan'" + ' and square_meters is not null and square_meters between 51 and 65 THEN 1 END) AS count3, ' \
                  'COUNT(CASE WHEN type like ' + "'stan'" + ' and square_meters is not null and square_meters between 66 and 80 THEN 1 END) AS count4,' \
                  'COUNT(CASE WHEN type like ' + "'stan'" + ' and square_meters is not null and square_meters between 81 and 95 THEN 1 END) AS count5, ' \
                  'COUNT(CASE WHEN type like ' + "'stan'" + ' and square_meters is not null and square_meters between 96 and 110 THEN 1 END) AS count6, ' \
                  'COUNT(CASE WHEN type like ' + "'stan'" + ' and square_meters is not null and 111 <= square_meters THEN 1 END) AS count7 ' \
                  'FROM "Realty";'

            cursor.execute(query)
            with open("visualization/appartment_square_meters.csv", "w", newline='') as csv_file:
                csv_writer=csv.writer(csv_file)
                csv_writer.writerow([i[0] for i in cursor.description])  # write headers
                csv_writer.writerows(cursor)

            # C)
            query='SELECT COUNT(CASE WHEN year_built is not null and year_built between 1950 and 1959 THEN 1 END) AS count1, ' \
                  'COUNT(CASE WHEN year_built is not null and year_built between 1960 and 1969 THEN 1 END) AS count2, ' \
                  'COUNT(CASE WHEN year_built is not null and year_built between 1970 and 1979 THEN 1 END) AS count3, ' \
                  'COUNT(CASE WHEN year_built is not null and year_built between 1980 and 1989 THEN 1 END) AS count4,' \
                  'COUNT(CASE WHEN year_built is not null and year_built between 1990 and 1999 THEN 1 END) AS count5, ' \
                  'COUNT(CASE WHEN year_built is not null and year_built between 2000 and 2009 THEN 1 END) AS count6, ' \
                  'COUNT(CASE WHEN year_built is not null and year_built between 2010 and 2019 THEN 1 END) AS count7 ' \
                  'FROM "Realty";'

            cursor.execute(query)
            with open("visualization/year_built_statistics.csv", "w", newline='') as csv_file:
                csv_writer=csv.writer(csv_file)
                csv_writer.writerow([i[0] for i in cursor.description])  # write headers
                csv_writer.writerows(cursor)

            # D)
            cities_query='select city from "Realty" group by city order by count(realty_id) desc limit 5;'
            cursor.execute(cities_query)
            cities = cursor.fetchall()
            rows = []
            for city in cities:
                query='select countSelling, ' \
                      'countRenting, ' \
                      'CAST((countSelling * 100) AS float) / (countSelling + countRenting) AS sellingPercentage, ' \
                      'CAST((countRenting * 100) AS float) / (countSelling + countRenting) AS rentingPercentage, ' \
                      'CAST((countRenting) AS float) / countSelling AS ratio, ' \
                      'city from ' \
                      '(select COUNT(CASE WHEN offer_type is not null and offer_type like ' + "'prodaja'" + ' THEN 1 END) AS countSelling, ' \
                      'COUNT(CASE WHEN offer_type is not null and offer_type like ' + "'izdavanje'" + ' THEN 1 END) AS countRenting, ' \
                      'city ' \
                      'FROM "Realty" where city like ' + "'" + city[0] + "'" + ' group by city) as tempTable;'
                cursor.execute(query)
                result = cursor.fetchall()
                rows.append(result[0])
            with open("visualization/ratio.csv", "w", newline='') as csv_file:
                csv_writer=csv.writer(csv_file)
                csv_writer.writerow([i[0] for i in cursor.description])  # write headers
                csv_writer.writerows(rows)

            # E)
            query='SELECT count1, ' \
                  'CAST((count1 * 100) AS float) / (count1 + count2 + count3 + count4 + count5) AS count1Percentage, ' \
                  'count2, ' \
                  'CAST((count2 * 100) AS float) / (count1 + count2 + count3 + count4 + count5) AS count2Percentage, ' \
                  'count3, ' \
                  'CAST((count3 * 100) AS float) / (count1 + count2 + count3 + count4 + count5) AS count3Percentage, ' \
                  'count4, ' \
                  'CAST((count4 * 100) AS float) / (count1 + count2 + count3 + count4 + count5) AS count4Percentage, ' \
                  'count5, ' \
                  'CAST((count5 * 100) AS float) / (count1 + count2 + count3 + count4 + count5) AS count5Percentage ' \
                  'From ' \
                '(SELECT COUNT(CASE WHEN price is not null and price <= 49999 THEN 1 END) AS count1, ' \
                  'COUNT(CASE WHEN price is not null and price between 50000 and 99999 THEN 1 END) AS count2, ' \
                  'COUNT(CASE WHEN price is not null and price between 100000 and 149999 THEN 1 END) AS count3, ' \
                  'COUNT(CASE WHEN price is not null and price between 150000 and 199999 THEN 1 END) AS count4,' \
                  'COUNT(CASE WHEN price is not null and price >= 200000 THEN 1 END) AS count5 ' \
                  'FROM "Realty" where offer_type like ' + "'prodaja'" + ') as tempTable;'

            cursor.execute(query)
            with open("visualization/price_stats.csv", "w", newline='') as csv_file:
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

    get_analysis()
