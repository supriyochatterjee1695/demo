import pandas as pd
df = pd.read_csv('dashboard.csv')
pivot_df = df.pivot_table(index=['Section', 'Parameters'])
pivot_df=pivot_df.drop(['Count'], axis=1)