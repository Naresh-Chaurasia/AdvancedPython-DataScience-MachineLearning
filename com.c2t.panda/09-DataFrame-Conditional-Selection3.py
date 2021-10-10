import pandas as pd
import  numpy  as np
from numpy.random import randn

np.random.seed(101)

df3 = pd.DataFrame(randn(5,4),['r1','r2','r3','r4','r5'],['c1','c2','c3','c4'])
print('------------------df3-------------------------')
print(df3)

#print(df3[df3['c1']>0][['c2','c1']])

print('------------------df3 with and condition-------------------------')
print(df3[(df3['c1']>0) & (df3['c2']>0) ] [['c1','c2']])


print(True and False)


