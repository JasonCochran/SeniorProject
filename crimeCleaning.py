# Requires Python 3.6 and pandas

import pandas as pd

df = pd.read_csv('crimeCSV/Crimes_-_2001_to_present.csv')

print("Rows before: ") 
print(df.shape)

df = df.dropna()

print("Rows after removing ALL NA's: ")
print(df.shape)

df.to_csv('crimeCSV/crimeCleaned.csv', index=False)
