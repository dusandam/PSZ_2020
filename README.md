# Real Estate Price predictor

---
## Abstract
This project is focused on the end-to-end data science lifecycle, using real estate data as its foundation. The process begins with scraping property listings from various Serbian real estate websites. This collected data is then used to perform comprehensive analysis, data visualization, and to build machine learning models for tasks such as price prediction and multi-class classification. The ultimate goal is to uncover hidden knowledge and patterns within the real estate market data.
---

## Task 1: Data Collection

To complete this phase, the `populate_database.py` script was used along with `repository.py`. The database was created with the `create_database.py` script, and its content is located in the `/analysis.database.csv` file.

---

## Task 2: Data Analysis

The results of this task are obtained by running the `analysis.py` script and are located in the `analysis` directory in the following files:

* A) `offer_count.csv`
* B) `listings_per_city.csv`
* C) `registered.csv`, `unregistered.csv`
* D) `expensive_houses.csv`, `expensive_appartments.csv`
* E) `expensive_houses_rent.csv`, `expensive_appartments_rent.csv`
* F) `bulit_in_2019.csv`
* G) `most_rooms.csv`, `most_bathrooms.csv`, `largest_land_area.csv`

---

## Task 3: Data Visualization

The results of this task are obtained by running the `visual_analysis.py` script and are located in the `visualization` directory in the following files:

* A) `most_present_quarters.csv`, `most_present_quarters.png`
* B) `appartment_square_meters.csv`, `appartment_square_meters.png`
* C) `year_built_statistics.csv`, `year_built_statistics.png`
* D) `ratio.csv`, `ratio_listings_percentage.png`, `ratio_number_of_listings.png`, `ratio_ratio.png`
* E) `price_stats.csv`, `price_stats.png`, `price_stats_percentage.png`

---

## Task 4: Linear Regression Implementation

The linear regression model was implemented with the `linear_regression.py` script, and the results were obtained by running the `test_regression.py` script. The script takes mandatory float arguments: `-y` (apartment year of construction, e.g., 2009) and `-s` (apartment square footage, e.g., 150). As a result, this script will output the general regression performance in the form of the mean squared error (MSE) obtained by comparing the actual values of the test dataset with the values predicted by the model. The error was evaluated on the normalized values of this data (between -1 and 1). The second result is the prediction of the apartment price for the given input data.

---

## Task 5: Support Vector Machine Algorithm Implementation

The Support Vector Machine algorithm with two kernel functions performs multi-class classification on the input dataset (properties for sale). It was implemented using the `sklearn` package. The script takes mandatory float arguments: `-y` (apartment year of construction, e.g., 2009), `-s` (apartment square footage, e.g., 150), and `-t` (total number of rooms, e.g., 4). The output values are divided into several classes: `'under_50'`, `'50_to_100'`, `'100_to_150'`, `'150_to_200'`, `'over_200'`, depending on the price range of the property. Two kernel functions were used for this algorithm: linear and polynomial. The results of this phase include the performance of the algorithm with each kernel function on the test dataset. The second result is the classification based on the input data.
