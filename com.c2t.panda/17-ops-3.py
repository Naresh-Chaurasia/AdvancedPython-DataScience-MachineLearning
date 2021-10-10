import pandas as pd
import numpy as np

df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,777],'col3':['abc','def','ghi','xyz']})
df.head()

def times2(x):
    return x*2

print('-------------------------df---------------------')
print(df)

print('--------------------------apply(times2)--------------------')
print(df['col1'].apply(times2))

print('--------------------------apply(len)-----------------------')
print(df['col3'].apply(len))

print('--------------------------drop-----------------------')
print(df.drop('col1',axis=1))

print('-------------------------df---------------------')
print(df)

print('-------------------------df.columns---------------------')
print(df.columns)

print('-------------------------df.index---------------------')
print(df.index)

print('-------------------------del---------------------')
del df['col1']
print(df)

print('-------------------------sort_values---------------------')
#print(df.sort_values(by='col2'))
print(df.sort_values('col2'))

print('-------------------------isnull---------------------')
print(df.isnull())
