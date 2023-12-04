import matplotlib.pyplot as plt
import pandas as pd

print(pd.__version__)

df = pd.read_csv('cali_data.csv')
df.set_index('Year').plot(title='California Fuel Type Vehicle Growth')
plt.show()
