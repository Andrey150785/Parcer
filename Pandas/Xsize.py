import pandas as pd

df = pd.read_csv('data.csv', encoding='1251')
# print(df.columns)

our_colums = ['DR_Dat', 'DR_Tim', 'DR_NDoc', 'DR_Kkm']
df = df[our_colums]
print(df)