# Requires Python 3.6 and pandas

import pandas as pd

df = pd.read_csv('crimeCSV/Crimes_-_2001_to_present.csv')

print(df.shape)
df = df.dropna()
print(df.shape)
df.to_csv('crimeCSV/crimeCleaned.csv', index=False)
