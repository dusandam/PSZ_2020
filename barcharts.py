import subprocess
import sys
from pathlib import Path
import numpy as np

if sys.version_info[:2] < (3, 0):
    code=subprocess.call(['python3'] + sys.argv)
    raise SystemExit(code)

import matplotlib.pyplot as plt
import pandas as pd
import os

visualization_directory="./visualization"

dirpath=os.path.abspath(visualization_directory)
all_files=[
    '/home/dusandam/Documents/projects/PSZProjekat/visualization/appartment_square_meters.csv',
    '/home/dusandam/Documents/projects/PSZProjekat/visualization/most_present_quarters.csv',
    '/home/dusandam/Documents/projects/PSZProjekat/visualization/price_stats.csv',
    '/home/dusandam/Documents/projects/PSZProjekat/visualization/ratio.csv',
    '/home/dusandam/Documents/projects/PSZProjekat/visualization/year_built_statistics.csv'
]

all_patterns=[]
index=0


def visualize_quarters(filepath):
    file=pd.read_csv(filepath)
    df=pd.DataFrame(file)
    print(df)
    column_name=[]
    x_value=[]
    val=[]

    quarters=df['quarter']
    count=df['count']

    for i in range(len(quarters)):
        x_value.append(str(df.iloc[i, 0]))

    for i in range(len(count)):
        val.append(int(df.iloc[i, 1]))

    test_name="File name: " + Path(filepath).stem

    plt.figure(9)

    plt.bar(quarters[:], count[:])

    plt.title(test_name)
    plt.xlabel('Deo grada')
    plt.ylabel('Broj nekretnina')

    plt.show()


def visualize_ratio(filepath):
    file=pd.read_csv(filepath)
    df=pd.DataFrame(file)
    barWidth=0.1
    countselling=[]
    countrenting=[]
    sellingpercentage=[]
    rentingpercentage=[]
    ratio=[]
    city=[]

    count_selling=df['countselling']
    count_renting=df['countrenting']
    selling_percentage=df['sellingpercentage']
    renting_percentage=df['rentingpercentage']
    ratios=df['ratio']
    cities=df['city']

    for i in range(len(count_selling)):
        countselling.append(int(df.iloc[i, 0]))

    for i in range(len(count_renting)):
        countrenting.append(int(df.iloc[i, 1]))

    for i in range(len(selling_percentage)):
        sellingpercentage.append(float(df.iloc[i, 2]))

    for i in range(len(renting_percentage)):
        rentingpercentage.append(float(df.iloc[i, 3]))

    for i in range(len(ratios)):
        ratio.append(float(df.iloc[i, 4]))

    for i in range(len(cities)):
        city.append(str(df.iloc[i, 5]))

    test_name="File name: " + Path(filepath).stem + ", numer of listings"

    plt.figure(11)
    r1=np.arange(len(count_selling))
    r2=[x + barWidth for x in r1]

    # Create blue bars
    plt.bar(r1, countselling[:], width=barWidth, color='blue', edgecolor='black', capsize=7, label='prodaja')

    # Create cyan bars
    plt.bar(r2, countrenting[:], width=barWidth, color='cyan', edgecolor='black', capsize=7, label='izdavanje')

    plt.xticks([r + barWidth for r in range(len(count_selling))], city[:])

    plt.title(test_name)
    plt.xlabel('Grad')
    plt.ylabel('Broj nekretnina')
    plt.legend()

    plt.show()

    test_name="File name: " + Path(filepath).stem + ", listings percentage"

    plt.figure(12)
    r1=np.arange(len(sellingpercentage))
    r2=[x + barWidth for x in r1]

    # Create blue bars
    plt.bar(r1, sellingpercentage[:], width=barWidth, color='blue', edgecolor='black', capsize=7, label='prodaja')

    # Create cyan bars
    plt.bar(r2, countrenting[:], width=barWidth, color='cyan', edgecolor='black', capsize=7, label='izdavanje')

    plt.xticks([r + barWidth for r in range(len(count_selling))], city[:])

    plt.title(test_name)
    plt.xlabel('Grad')
    plt.ylabel('Procenat')
    plt.legend()

    plt.show()

    test_name="File name: " + Path(filepath).stem + ", ratio"
    plt.figure(13)

    plt.bar(city[:], ratio[:])


    plt.title(test_name)
    plt.xlabel('Grad')
    plt.ylabel('Odnos')
    plt.show()


    # test_name="File name: " + Path(filepath).stem + ", listing percentage"
    #
    # plt.figure(12)
    #
    # plt.bar(quarters[:], city[:])
    #
    # plt.title(test_name)
    # plt.xlabel('Deo grada')
    # plt.ylabel('Broj nekretnina')
    #
    # plt.show()
    #
    # test_name="File name: " + Path(filepath).stem + ", listing ratio"
    #
    # plt.figure(13)
    #
    # plt.bar(ratio[:], city[:])
    #
    # plt.title(test_name)
    # plt.xlabel('Deo grada')
    # plt.ylabel('Broj nekretnina')
    #
    # plt.show()


def visualize_price_stats(filepath):
    file=pd.read_csv(filepath)
    df=pd.DataFrame(file)
    print(df)
    column_name=[]
    percentage_column_name=[]
    all_col_names=[]
    percentage_value=[]
    val=[]

    for column in df:
        all_col_names.append(column)
        if ('percentage' in column):
            percentage_column_name.append(column)
        else:
            column_name.append(column)

    for i in range(len(all_col_names)):
        if ('percentage' in all_col_names[i]):
            percentage_value.append(float(df.iloc[0, i]))
        else:
            val.append(int(df.iloc[0, i]))

    test_name="File name: " + Path(filepath).stem

    index=21
    plt.figure(index)
    plt.bar(column_name[:], val[:])

    plt.title(test_name)
    plt.xlabel('Variant')
    plt.ylabel('Number')
    plt.show()

    test_name="File name: " + Path(filepath).stem + " percentage"

    index=22
    plt.ylim(100)
    plt.figure(index)

    plt.bar(percentage_column_name[:], percentage_value[:])

    plt.title(test_name)
    plt.xlabel('Variant')
    plt.ylabel('Percentage')
    plt.show()


for filepath in all_files:
    if 'most_present_quarters' in filepath:
        visualize_quarters(filepath)
        continue
    if 'ratio' in filepath:
        visualize_ratio(filepath)
        continue
    if 'price_stats' in filepath:
        visualize_price_stats(filepath)
        continue
    file=pd.read_csv(filepath)
    df=pd.DataFrame(file)
    print(df)
    column_name=[]
    x_value=[]
    val=[]

    for column in df:
        column_name.append(column)

    for i in range(len(column_name)):
        val.append(float(df.iloc[0, i]))

    test_name="File name: " + Path(filepath).stem

    index=index + 1
    plt.figure(index)

    plt.bar(column_name[:], val[:])

    plt.title(test_name)
    plt.xlabel('X')
    plt.ylabel('Y')

    plt.show()
