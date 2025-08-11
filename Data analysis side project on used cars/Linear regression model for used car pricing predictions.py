import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import sys
import os
import csv


def creating_csv():
    file_path = "saved_price_predictions.csv"
    if os.path.exists(file_path):
        print("Save file exists")
    else:
        with open('saved_price_predictions.csv', 'w') as file:
            pass


def creating_and_training_prediction_model():
    # creating and training linear regression model for predicting used car prices
    model_df = pd.read_csv('mapped_vehicles.csv')
    X = model_df[['year', 'condition', 'cylinders', 'manufacturer']]
    y = model_df['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    used_car_price_model = LinearRegression()
    used_car_price_model.fit(X_train, y_train)
    return used_car_price_model


def manufacturer_to_value_conversion(manufacturer: str) -> int:
    # maps manufacturer text to specified value for model based on average price of manufacturers vehicles
    manufacturer = str(input("Enter manufacturer name: "))
    manufacturer = manufacturer.lower()
    manufacturer_dict = {'saturn': 1, 'mercury': 2, 'pontiac': 3, 'chrysler': 4, 'honda': 5, 'hyundai': 6, 'fiat': 7, 'kia': 8, 'nissan': 9, 'morgan': 10, 
                        'volkswagen': 11, 'mazda': 12, 'harley-davidson': 13, 'subaru': 14, 'mitsubishi': 15, 'mini': 16, 'dodge': 17, 'land rover': 18, 'buick': 19, 'datsun': 20,
                        'toyota': 21, 'volvo': 22, 'ferrari': 23, 'chevrolet': 24, 'jeep': 25, 'ford': 26, 'cadillac': 27, 'lincoln': 28, 'bmw': 29, 'mercedes-benz': 30,
                        'lexus': 31, 'acura': 32, 'infiniti': 33, 'gmc': 34, 'audi': 35, 'rover': 36, 'porsche': 37, 'jaguar': 38, 'aston-martin': 39, 'ram': 40,
                        'alfa-romeo': 41, 'tesla': 42}
    if manufacturer not in manufacturer_dict:
        print('Manufacturer name incorrect or not included in model')
        manufacturer_to_value_conversion()
    else:
        man_value = manufacturer_dict[manufacturer]
        return man_value

def condition_to_value_conversion(condition: str) -> int:
    # maps condition text to speicified value for model based on average price of condition
    condition = str(input("Enter condition of vehicle (salvage, fair, good, excellent, like new or new): "))
    condition = condition.lower()
    condition_dict = {'salvage': 1, 'fair': 2, 'good': 6, 'excellent': 3, 'like new': 4, 'new': 5}
    if condition not in condition_dict:
        print('Condition incorrect or not included in model')
        condition_to_value_conversion()
    else:
        cond_value = condition_dict[condition]
        return cond_value

def cylinder_to_value_conversion(cylinder: str) -> int:
    # maps cylinder count to specified value for model based on average price of condition
    cylinder = str(input("Enter number of cylinders in vehicle (try typing other if value incorrect):"))
    cylinder_dict = {'3': 3, '4': 2, '5': 1, 'other': 4, '10': 5, '6': 6, '12': 7, '8': 8}
    if cylinder not in cylinder_dict:
        print('Cylinder value incorrect or not included in model')
        cylinder_to_value_conversion()
    else:
        cyl_value = cylinder_dict[cylinder]
        return cyl_value
    
def get_year_value() -> float:
    year = float(input("Enter year of vehicle (between 1900 and 2021): "))
    if year < 1900 or year > 2021:
        print("Year value out of bounds for model")
        get_year_value()
    else:
        return year

def used_car_price_prediction(mapped_manufacturer: int, mapped_condition: int, mapped_cylinder: int, year: int, model: LinearRegression):
    used_car_df = {
        'year': [year],
        'condition': [mapped_condition],
        'cylinders': [mapped_cylinder],
        'manufacturer': [mapped_manufacturer]
    }
    used_car_data = used_car_df[['year', 'condition', 'cylinders', 'manufacturer']]
    price_predict = model.predict(used_car_data)
    return price_predict



def model_main_function():
    model = creating_and_training_prediction_model()
    while 1 == 1:
        details_to_save = {
        'year': [],
        'condition': [],
        'cylinders': [],
        'manufacturer': [],
        'predicted price': []
        }
        print("/n/n/n")
        creating_csv()
        price_request = str(input("Would you like to predict a price for your car or view previous results: "))
        price_request = price_request.lower()
        if price_request == "yes":
            mapped_manufacturer = manufacturer_to_value_conversion()
            details_to_save['manufacturer'] = mapped_manufacturer
            mapped_condition = condition_to_value_conversion()
            details_to_save['condition'] = mapped_condition
            mapped_cylinder = cylinder_to_value_conversion()
            details_to_save['cylinders'] = mapped_cylinder
            year = get_year_value()
            details_to_save['year'] = year
            predicted_price = used_car_price_prediction(mapped_manufacturer, mapped_condition, mapped_cylinder, year, model)
            details_to_save['predicted price'] = predicted_price
            print(f'predicted price for car is: £{predicted_price}')
            details_to_save.to_csv('saved_price_predictions.csv', mode = 'a')
        elif price_request == "no":
            sys.exit()
        elif price_request == "view previous results":
            with open('saved_price_predictions.csv', mode='r') as file:
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    print(row)
        else:
            print("Invalid option, try yes, no or view previous results")
model_main_function()