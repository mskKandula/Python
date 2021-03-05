import pandas as pd

url = 'https://www.presidentsusa.net/presvplist.html'

data = pd.read_html(url)

df = data[0]

# print(df.columns)

df = df.drop(axis=1,columns='Unnamed: 3')

print(df.head())