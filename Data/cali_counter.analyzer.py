import pandas as pd
import sys

print(pd.__version__)

datasets = {
    'cali_2018': 'State of California- Vehicle Fuel Type Count by ZIP Code OCTOBER 2018.csv',
    'cali_2020': 'State of California- Vehicle Fuel Type Count by ZIP Code JANUARY 2020.csv',
    'cali_2021': 'State of California- Vehicle Fuel Type Count by ZIP Code JANUARY 2021.csv',
    'cali_2022': 'State of California- Vehicle Fuel Type Count by ZIP Code JANUARY 2022.csv',
    'cali_2023': 'State of California- Vehicle Fuel Type Count by ZIP Code JANUARY 2023.csv',
}

try:
    argv_1 = sys.argv[1]
except:
    dataset = input(f'Options for datasets:\n{datasets}\n')
else:
    dataset = sys.argv[1]

df = pd.read_csv(datasets[dataset])

# print(df.loc[df['Fuel'] == 'Unk'])
print(df.groupby('Fuel').size())