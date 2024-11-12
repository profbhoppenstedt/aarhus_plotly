import pandas as pd

df = pd.read_csv('test.csv')

filtered_df = df[df['Pclass'] == 1]

print(filtered_df.head())