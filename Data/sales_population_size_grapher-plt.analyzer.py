import pandas as pd
import matplotlib.pyplot as plt

x = int(input('Input number:\n1. 10301_hev+sale+2-28-20.xlsx\n2. 10567_pev_sales_2-28-20.xlsx\n'))

df = None

if x == 1:
    df = pd.read_excel('10301_hev_sale_2-28-20.xlsx')
elif x == 2:
    df = pd.read_excel('10567_pev_sales_2-28-20.xlsx')

print(df.head(5))
# df.drop().plot()
# plt.show()

# plt.rcParams['figure.autolayout'] = True

# h = df.columns.values

# df.set_index('Date').plot()

# plt.show()
