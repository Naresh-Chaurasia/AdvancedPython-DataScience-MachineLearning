import pandas as pd
import  numpy  as np
from numpy.random import randn

np.random.seed(101)

df3 = pd.DataFrame(randn(5,4),['r1','r2','r3','r4','r5'],['c1','c2','c3','c4'])
print('-------------------df3-----------------------')
print(df3)

print('----------------df3.iloc[0]----------------------')
print(df3.iloc[0])

df3_reset = df3.reset_index()
print('----------------df3_reset----------------------')
print(df3_reset)

print('----------------df3_reset.iloc[0]----------------------')
print(df3_reset.iloc[0])