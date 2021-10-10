import pandas as pd
import  numpy  as np
from numpy.random import randn

np.random.seed(101)

df3 = pd.DataFrame(randn(5,4),['r1','r2','r3','r4','r5'],['c1','c2','c3','c4'])
print('-------------------df3-----------------------')
print(df3)
#print(df3.loc['r1'])


df3_reset_index = df3.reset_index()
print('-------------------df3_reset_index-----------------------')
print(df3_reset_index)

print('-------------------df3_reset_index.iloc[0]-----------------------')
print(df3_reset_index.iloc[0])



print('-------------------------------------------')
#print(df3_reset_index.loc['r1'])

#print(df3_reset_index.c2)

#print(df3.reset_index(inplace=True))


'''
df3.reset_index(inplace=True)
print(df3)
print(df3.iloc[1])
'''

