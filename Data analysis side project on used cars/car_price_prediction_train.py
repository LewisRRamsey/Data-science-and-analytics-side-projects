# Round odometer to nearest 1000 for accuracy balance
# Use year, condition, cylinder, manufacturer and odometer from mapped vehicles
# Split into test and train split
# Train model
# Test model
# Evaluate model

from pymongo import MongoClient
import pandas as pd
import numpy as np

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

from sklearn.model_selection import train_test_split

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


# removing unnecessary data from used car dataframe, leaving price, mileage, condition, cylinders, manufacturer and year
def decomposing_used_car_data(mapped_vehicles_df: pd.DataFrame):
    decomp_vehicles_df = mapped_vehicles_df[['price', 'year', 'manufacturer', 'condition', 'cylinders', 'odometer']]
    return decomp_vehicles_df

# splitting data randomly into test and training data using a 90/10 split
def split_test_and_train_data(decomp_vehicles_df):
    None
    x = decomp_vehicles_df.drop(columns=['price']).values
    y = decomp_vehicles_df['price'].values
    y = y.reshape(-1, 1)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=42)
    return x_train, x_test, y_train, y_test


# preparing data

mapped_vehicles_df = get_used_car_dataset()
decomp_vehicles_df = decomposing_used_car_data(mapped_vehicles_df)
x_train, x_test, y_train, y_test = split_test_and_train_data(decomp_vehicles_df)


