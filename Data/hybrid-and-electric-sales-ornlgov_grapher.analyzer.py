import pandas as pd
import matplotlib.pyplot as plt
import re

df = pd.read_csv('hybrid-and-electric-sales-ornlgov.csv')

df.set_index('Calendar year').drop(['Hybrid share of all light vehicles', 'Plug-in hybrid share of all light vehicles',
                                    'All-electric share of all light vehicles'], axis=1).plot(title='Growth of types of hybrid and electric vehicles')

for i in 'Hybrid share of all light vehicles', 'Plug-in hybrid share of all light vehicles', 'All-electric share of all light vehicles':
    df[i] = df[i].map(lambda x: float(x.rstrip('%')))
df['All light vehicle sales (thousands)'] = df['All light vehicle sales (thousands)'].replace({'"': '', ',': ''},
                                                                                              regex=True)
df.astype({'All light vehicle sales (thousands)': 'int32'})

share_df = df[['Calendar year', 'Hybrid share of all light vehicles', 'Plug-in hybrid share of all light vehicles',
               'All-electric share of all light vehicles']].copy()
share_df['Other fuel type share of all light vehicles'] = 0.0
for i in range(share_df.shape[0]):
    share_df['Other fuel type share of all light vehicles'][i] = float(
        100 - share_df.iloc[i, 1] - share_df.iloc[i, 2] - share_df.iloc[i, 3])

share_df.reset_index(drop=True).T.plot(kind='pie', y=22, title='Hybrid and electric sales percentage, 2021')

print(share_df.head(23))
plt.show()
