import psycopg2
import csv

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt

class TestRegression:

    def prepare_data():
        connection=None
        try:
            connection=psycopg2.connect(user="dusandam",
                                        password="dusandam",
                                        host="localhost",
                                        port="5432",
                                        database="nekretnine")

            cursor=connection.cursor()

            # A)
            for_sale_query='select * from "Realty" where ' \
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

    def normalize(X):
        min = np.amin(X)
        max = np.amax(X)
        X = ((X - min) * 2 )/ (max - min) - 1
        return X

    prepare_data()
    # read data
    df=pd.read_csv("appartments_for_sale_belgrade.csv")[['square_meters', 'year_built', 'price']].dropna()
    # df=(df - df.mean()) / df.std()
    Y=df['price'].astype(float)
    Y = normalize(Y)
    # divide data to test and train sets
    X1 = df[['square_meters', 'year_built']].astype(float)
    X1 = normalize(X1)
    X1_train, X1_test=train_test_split(X1, test_size=0.2, random_state=1)
    Y_train, Y_test=train_test_split(Y, test_size=0.2, random_state=1)


    # normalize values
    regressor=LinearRegression(learning_rate=0.001, n_iters=1000)
    regressor.fit(X1_train, Y_train)
    predictions=regressor.predict(X1_test)

    mse=mean_squared_error(Y_test, predictions)
    print("MSE:", mse)
    plt.show()
