import pandas as pd
import  numpy  as np
from numpy.random import randn

np.random.seed(101)

df3 = pd.DataFrame(randn(5,4),['r1','r2','r3','r4','r5'],['c1','c2','c3','c4'])
print(df3)
print('----------------------------------------')

#df3.drop('c4')
#https://stackoverflow.com/questions/22149584/what-does-axis-in-pandas-mean
df3.drop('c4',axis=1,inplace=True)
print('----------------------------------------')
print(df3)