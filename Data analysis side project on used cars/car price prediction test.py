def manufacturer_to_value_conversion():
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
        return man_value, manufacturer

def condition_to_value_conversion():
    # maps condition text to speicified value for model based on average price of condition
    condition = str(input("Enter condition of vehicle (salvage, fair, good, excellent, like new or new): "))
    condition = condition.lower()
    condition_dict = {'salvage': 1, 'fair': 2, 'good': 6, 'excellent': 3, 'like new': 4, 'new': 5}
    if condition not in condition_dict:
        print('Condition incorrect or not included in model')
        condition_to_value_conversion()
    else:
        cond_value = condition_dict[condition]
        return cond_value, condition

def cylinder_to_value_conversion():
    # maps cylinder count to specified value for model based on average price of condition
    cylinder = str(input("Enter number of cylinders in vehicle (try typing other if value incorrect):"))
    cylinder_dict = {'3': 3, '4': 2, '5': 1, 'other': 4, '10': 5, '6': 6, '12': 7, '8': 8}
    if cylinder not in cylinder_dict:
        print('Cylinder value incorrect or not included in model')
        cylinder_to_value_conversion()
    else:
        cyl_value = cylinder_dict[cylinder]
        return cyl_value, cylinder
    
def get_year_value() -> float:
    # retrieves year from mapped dataframe and checks for suitability
    year = float(input("Enter year of vehicle (between 1900 and 2021): "))
    if year < 1900 or year > 2021:
        print("Year value out of bounds for model")
        get_year_value()
    else:
        return year
    
def get_odometer_value() -> float:
    #retrieves odometer value from dataframe and checks suitability
    odometer = float(input("Enter mileage of vehicle: "))
    if odometer < 0:
        print("Negative mileage not possible")
        get_odometer_value()
    else:
        return odometer