import pandas as pd
import  numpy  as np
from numpy.random import randn

np.random.seed(101)

df3 = pd.DataFrame(randn(5,4),['r1','r2','r3','r4','r5'],['c1','c2','c3','c4'])
print(df3)
print('')
print('')

bool_df3 = df3>0

print('bool_df3=')
print(bool_df3)
print('')
print('-------------------------------------------')
print('df3[bool_df3]=')
print(df3[bool_df3])

print('-------------------------------------------')
df3_nan = df3[bool_df3]
print(df3_nan.dropna())
print('-------------------------------------------')

print(df3[df3>0])