import pandas as pd
import  numpy  as np
from numpy.random import randn

np.random.seed(101)

rows = ['r1','r2','r3','r4','r5']
cols = ['c1','c2','c3','c4']

df1 = pd.DataFrame(randn(5,4),rows,cols)
print('2 Dimensional array \n',df1)

print('-----------')
print(df1.drop('c2',axis=1,inplace=True))
print('-----------')
print(df1)







