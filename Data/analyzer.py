import pandas as pd
import sys

print(pd.__version__)

def file_choose(dataset):
    if dataset == 'chicago':
        return 'City of Chicago Traffic Crashes - Crashes.csv'
    elif dataset == 'nyc':
        return 'New York City- NYC EV Fleet Station Network.csv'
    elif dataset == 'cali_2018':
        return 'State of California- Vehicle Fuel Type Count by ZIP Code OCTOBER 2018.csv'
    elif dataset == 'cali_2020':
        return 'State of California- Vehicle Fuel Type Count by ZIP Code JANUARY 2020.csv'
    elif dataset == 'cali_2021':
        return 'State of California- Vehicle Fuel Type Count by ZIP Code JANUARY 2021.csv'
    elif dataset == 'cali_2022':
        return 'State of California- Vehicle Fuel Type Count by ZIP Code JANUARY 2022.csv'
    elif dataset == 'cali_2023':
        return 'State of California- Vehicle Fuel Type Count by ZIP Code JANUARY 2023.csv'
    elif dataset == 'connecticut':
        return 'State of Connecticut - Electric Vehicle Charging Stations.csv'
    elif dataset == 'washington_population':
        return 'State of Washington - Electric Vehicle Population Data.csv'
    elif dataset == 'washington_ev_registration':
        return 'State of Washington - Electric Vehicle Title and Registration Activity.csv'
    elif dataset == 'epa_trends':
        return 'United States Environmental Protection Agency – Automotive Trends Report.csv'
    elif dataset == 'doe_inventory':
        return 'US Department of Energy - City and County Vehicle Inventories.xlsb'

if sys.argv[1] == 'doe_inventory':
    df = pd.read_excel(file_choose(sys.argv[1]))    
else:
    df = pd.read_csv(file_choose(sys.argv[1]))
    
print(df)
