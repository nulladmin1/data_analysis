import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Electric_Vehicle_Population_Size_History(data.wa.gov).csv')

plt.rcParams['figure.autolayout'] = True

h = df.columns.values

df.set_index('Date').plot(title='Washington Electric Vehicle Population Size Growth')

plt.show()