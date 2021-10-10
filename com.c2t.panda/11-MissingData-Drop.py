import numpy as np
import pandas as pd


map1= {'A':[1,2,np.nan],
                  'B':[5,np.nan,np.nan],
                  'C':[1,2,3]}

df = pd.DataFrame(map1)
print(df)

print('--------df.dropna()------------')
#print(df.dropna(inplace=True))


print('--------df------------')
#print(df)

print('--------Dropping Cols------------')
print(df.dropna(axis=1))

print('--------Threshold------------')
print(df.dropna(axis=1,thresh=2))
