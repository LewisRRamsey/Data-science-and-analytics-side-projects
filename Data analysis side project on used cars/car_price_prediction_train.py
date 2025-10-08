# Round odometer to nearest 1000 for accuracy balance
# Use year, condition, cylinder, manufacturer and odometer from mapped vehicles
# Split into test and train split
# Train model
# Test model
# Evaluate model

from pymongo import MongoClient
import pandas as pd

import torch
import torch.nn as nn
import torch.nn.functional as F

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
def decomposing_used_car_data(mapped_vehicles_df):
    None


# splitting data randomly into test and training data using a 90/10 split
def split_test_and_train_data(decomp_vehicles_df):
    None

    
class UsedCarPricePredictor(nn.Module):
    
    def __init__(self):
        super(UsedCarPricePredictor, self).__init__()
        self.input_layer = nn.Linear(5, 128)
        self.hidden_layer1 = nn.Linear(128, 64)
        self.hidden_layer2 = nn.Linear(64, 32)
        self.hidden_layer3 = nn.Linear(32, 16)
        self.output_layer = nn.Linear(16, 1)

    def forward(self, data_input):
        data = F.relu(self.input_layer(data_input))
        data = F.relu(self.hidden_layer1(data))
        data = F.relu(self.hidden_layer2(data))
        data = F.relu(self.hidden_layer3(data))
        output_data = F.relu(self.output_layer(data))
        return output_data
    
    
    

# central function for training model and preparing data
def train_used_car_model():

    # preparing data

    mapped_vehicles_df = get_used_car_dataset
    

train_used_car_model()




