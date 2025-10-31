from pymongo import MongoClient
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

# Accessing dataset from MongoBD

def get_used_car_dataset():

    client = MongoClient("mongodb://localhost:27017/") 
    db = client["data"] 
    collection = db["mapped-vehicles"] 

    used_car_data = list(collection.find()) 
    mapped_vehicles_df = pd.DataFrame(used_car_data)

    # removing mongoDB id field
    if '_id' in mapped_vehicles_df.columns:
        mapped_vehicles_df = mapped_vehicles_df.drop(columns=['_id'])

    return mapped_vehicles_df


def decomposing_used_car_data(mapped_vehicles_df: pd.DataFrame):

    # removing unnecessary data from used car dataframe, leaving price, mileage, condition, cylinders, manufacturer and year

    decomp_vehicles_df = mapped_vehicles_df[['price', 'year', 'manufacturer', 'condition', 'cylinders', 'odometer']]
    return decomp_vehicles_df


def split_test_and_train_data(decomp_vehicles_df):

    # splitting data into test and training data using a 90/10 split

    x = decomp_vehicles_df.drop(columns=['price']).values
    y = decomp_vehicles_df['price'].values
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=42)
    return x_train, x_test, y_train, y_test


def creating_decision_tree(info_train, price_train):

    # creating random forest regressor model

    dt_price_model = RandomForestRegressor(random_state=42, max_depth = 23, max_features = 'sqrt', bootstrap = False, n_estimators = 100)
    dt_price_model.fit(info_train, price_train)
    return dt_price_model


def testing_decision_tree_model(dt_price_model, info_test, info_train, price_test, price_train, mapped_vehicles_df):

    # predicting prices with random forest regressor model
    price_pred_train = dt_price_model.predict(info_train)
    price_pred_test = dt_price_model.predict(info_test)

    # calculating mae model
    train_mae = mean_absolute_error(price_train, price_pred_train)
    test_mae = mean_absolute_error(price_test, price_pred_test)

    # calculating avg error %
    prices = mapped_vehicles_df['price']
    avg_price = np.mean(prices)
    avg_error_percentage_train = f'{(train_mae / avg_price) * 100}%'
    avg_error_percentage_test = f'{(test_mae / avg_price) * 100}%'

    # plotting table

    fig, ax = plt.subplots()
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(cellText = [[train_mae, avg_error_percentage_train], [test_mae, avg_error_percentage_test]], colLabels = ['MAE (£)', 'Average Error Percentage'], rowLabels = ['Train data', 'Test Data'], loc = 'center')
    plt.show()

def main():
    # collecting_data
    mapped_vehicles_df = get_used_car_dataset()
    decomp_vehicles_df = decomposing_used_car_data(mapped_vehicles_df)
    info_train, info_test, price_train, price_test = split_test_and_train_data(decomp_vehicles_df)
    
    # training price prediction model
    dt_price_model = creating_decision_tree(info_train, price_train)

    # testing price prediction model
    testing_decision_tree_model(dt_price_model, info_test, info_train, price_test, price_train, mapped_vehicles_df)

main()