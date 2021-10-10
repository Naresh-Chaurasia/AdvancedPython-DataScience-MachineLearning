import pandas as pd
import  numpy  as np
from numpy.random import randn

np.random.seed(101)

df1 = pd.DataFrame(randn(5,4),['r1','r2','r3','r4','r5'],['c1','c2','c3','c4'])
#print(df1)

print('--------------------------------------')

array_2d = [[1,2,3,4,5],
            [10,20,30,40,50],
            [100,200,300,400,500]
            ]
df2 = pd.DataFrame(array_2d)
#df2 = pd.DataFrame(array_2d,['r1','r2','r3'],['c1','c2','c3','c4','c5'])
print(df2)
print('--------------------------------------')
print(df2.shape)
print('--------------------------------------')
print(df2['c1'])
print(type(df2['c1']))
print('--------------------------------------')
print(type(df2))
