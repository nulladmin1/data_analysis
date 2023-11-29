import pandas as pd
import matplotlib.pyplot as plt

main_df = pd.read_csv('IEA-EV-dataEV salesHistoricalCars.csv')

usa_df = main_df.query('region == "USA" and parameter == "EV sales"')
print(usa_df.head(5))

usa_df.set_index('year').plot()

plt.show()