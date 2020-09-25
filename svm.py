import argparse
import csv

import pandas as pd
import psycopg2
from sklearn import svm
from sklearn.model_selection import train_test_split

parser=argparse.ArgumentParser()
parameters=parser.add_argument_group('required arguments')

parameters.add_argument("-y", "--year_built", type=float, required=True, metavar='', choices=range(1850, 2021))
parameters.add_argument("-s", "--square_meters", type=float, required=True, metavar='')
parameters.add_argument("-t", "--total_rooms", type=float, required=True, metavar='')

args=parser.parse_args()


class RunSvm:

    def prepare_data():
        connection=None
        try:
            connection=psycopg2.connect(user="dusandam",
                                        password="dusandam",
                                        host="localhost",
                                        port="5432",
                                        database="psz_realestate")

            cursor=connection.cursor()

            for_sale_query='select * from "realty" where ' \
                           'offer_type like ' + "'prodaja'"
            cursor.execute(for_sale_query)
            with open("for_sale.csv", "w", newline='') as csv_file:
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

    def classify(price):
        if price < 50000:
            return 'under_50'
        if price < 100000:
            return '50_to_100'
        if price < 150000:
            return '100_to_150'
        if price < 200000:
            return '150_to_200'
        else:
            return 'over_200'

    prepare_data()
    # read data
    df=pd.read_csv("for_sale.csv")[['square_meters', 'year_built', 'total_rooms', 'price']].dropna()
    Y=df['price'].astype(float)
    # classification of outputs
    for index, value in Y.items():
        Y[index]=classify(value)
    X1=df[['square_meters', 'year_built', 'total_rooms']].astype(float)
    X1_train, X1_test=train_test_split(X1, train_size=0.8, random_state=1)
    Y_train, Y_test=train_test_split(Y, train_size=0.8, random_state=1)

    # kernel functions
    linear=svm.SVC(kernel='linear', C=1, decision_function_shape='ovo').fit(X1_train, Y_train)
    polynomial=svm.SVC(kernel='poly', degree=3, C=1, decision_function_shape='ovo').fit(X1_train, Y_train)

    prediction_linear=linear.predict(X1_test)
    prediction_polynomial=polynomial.predict(X1_test)

    score_linear=linear.score(X1_test, Y_test)
    score_polynomial=polynomial.score(X1_test, Y_test)

    print('Linear Kernel score:', score_linear)
    print('Polynomial Kernel score:', score_polynomial)

    test_square_meters=args.square_meters
    test_year_built=args.year_built
    test_total_rooms=args.total_rooms
    data={'square_meters': [test_square_meters], 'year_built': [test_year_built], 'total_rooms': [test_total_rooms]}
    X=pd.DataFrame(data)
    input_linear_pred=linear.predict(X)
    input_poly_pred=polynomial.predict(X)

    print('Linear Kernel prediction:', input_linear_pred)
    print('Polynomial Kernel prediction:', input_poly_pred)
