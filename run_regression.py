import psycopg2
import csv
import argparse

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import datasets


parser=argparse.ArgumentParser()
parameters=parser.add_argument_group('required arguments')

parameters.add_argument("-y", "--year_built", type=float, required=True, metavar='', choices=range(1850, 2021))
parameters.add_argument("-s", "--square_meters", type=float, required=True, metavar='')

args=parser.parse_args()


class RunRegression:

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
                           'type like ' + "'stan'" + ' and offer_type like ' \
                           + "'prodaja'" + " and city like 'Beograd'"
            cursor.execute(for_sale_query)
            with open("appartments_for_sale_belgrade.csv", "w", newline='') as csv_file:
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

    from linear_regression import LinearRegression

    def mean_squared_error(y_true, y_pred):
        return np.mean((y_true - y_pred) ** 2)

    def normalize(X, min, max):
        X = ((X - min) * 2 ) / (max - min) - 1
        return X

    def un_normalize(X, Xmin, Xmax):
        X = (X + 1) * (Xmax - Xmin) / 2 + Xmin
        return X

    prepare_data()
    # read data
    df=pd.read_csv("appartments_for_sale_belgrade.csv")[['square_meters', 'year_built', 'price']].dropna()
    Y=df['price'].astype(float)
    Ymin=np.amin(Y)
    Ymax=np.amax(Y)
    Y = normalize(Y, Ymin, Ymax)
    X1 = df[['square_meters', 'year_built']].astype(float)
    Xmin=np.amin(X1)
    Xmax=np.amax(X1)
    X1 = normalize(X1, Xmin, Xmax)
    # divide data to test and train sets
    X1_train, X1_test=train_test_split(X1, test_size=0.2, random_state=1)
    Y_train, Y_test=train_test_split(Y, test_size=0.2, random_state=1)

    # normalize values
    regressor=LinearRegression(learning_rate=0.001, n_iters=1000)
    regressor.fit(X1_train, Y_train)
    predictions=regressor.predict(X1_test)

    mse=mean_squared_error(Y_test, predictions)
    print("MSE:", mse)
    predictions = un_normalize(predictions, Ymin, Ymax)

    test_square_meters = args.square_meters
    test_year_built = args.year_built
    data={'square_meters': [test_square_meters], 'year_built': [test_year_built]}

    X=pd.DataFrame(data)
    Xmin=np.minimum(Xmin, X)
    Xmax=np.maximum(Xmax, X)
    X = normalize(X, Xmin, Xmax)
    prediction_of_input = regressor.predict(X)
    prediction = un_normalize(prediction_of_input, Ymin, Ymax)
    print('Prediction: ' + str(prediction))
