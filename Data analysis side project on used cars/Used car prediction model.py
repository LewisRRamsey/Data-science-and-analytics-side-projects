def manufacturer_to_value_conversion(manufacturer: str):
    manufacturer_dict = {'saturn': 1, 'mercury': 2, 'pontiac': 3, 'chrysler': 4, 'honda': 5, 'hyundai': 6, 'fiat': 7, 'kia': 8, 'nissan': 9, 'morgan': 10, 
                        'volkswagen': 11, 'mazda': 12, 'harley-davidson': 13, 'subaru': 14, 'mitsubishi': 15, 'mini': 16, 'dodge': 17, 'land rover': 18, 'buick': 19, 'datsun': 20,
                        'toyota': 21, 'volvo': 22, 'ferrari': 23, 'chevrolet': 24, 'jeep': 25, 'ford': 26, 'cadillac': 27, 'lincoln': 28, 'bmw': 29, 'mercedes-benz': 30,
                        'lexus': 31, 'acura': 32, 'infiniti': 33, 'gmc': 34, 'audi': 35, 'rover': 36, 'porsche': 37, 'jaguar': 38, 'aston-martin': 39, 'ram': 40,
                        'alfa-romeo': 41, 'tesla': 42}
    man_value = manufacturer_dict[manufacturer]
    return man_value

def condition_to_value_conversion(condition: str):
    condition_dict = {'salvage': 1, 'fair': 2, 'good': 6, 'excellent': 3, 'like new': 4, 'new': 5}
    cond_value = condition_dict[condition]
    return cond_value

def cylinder_to_value_conversion(cylinder: str):
    cylinder_dict = {'3 cylinders': 3, '4 cylinders': 2, '5 cylinders': 1, 'other': 4, '10 cylinders': 5, '6 cylinders': 6, '12 cylinders': 7, '8 cylinders': 8}
    if cylinder not in cylinder_dict:
        return 'Cylinder value incorrect or not included in model'
    else:
        cyl_value = cylinder_dict[cylinder]
        return cyl_value

def used_car_price_prediction_model():
    None