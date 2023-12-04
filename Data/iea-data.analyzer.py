import pandas as pd
import matplotlib.pyplot as plt

main_df = pd.read_csv('IEA-EV-dataEV salesHistoricalCars.csv')

usa_df = main_df.query('region == "USA" and parameter == "EV sales"')

usa_df.drop(columns=['category', 'parameter', 'mode', 'unit']).set_index('year').sort_values('year').to_csv('IEA-EV-dataEV salesHistoricalCars_USA_EV-sales-sorted1.csv')

usa_df = pd.read_csv('IEA-EV-dataEV salesHistoricalCars_USA_EV-sales-sorted.csv').set_index('year').plot(title='US Historical Cars Sales')
plt.show()
