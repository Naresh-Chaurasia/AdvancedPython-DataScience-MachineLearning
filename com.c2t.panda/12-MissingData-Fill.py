import numpy as np
import pandas as pd


map1= {'A':[1,2,np.nan],
                  'B':[5,np.nan,np.nan],
                  'C':[1,2,3]}

df = pd.DataFrame(map1)
print(df)

print('--------Filling------------')
print(df.fillna(value='Filling'))

print('--------Filling Series------------')
print(df['A'].fillna(value='series'))

print('--------Filling Series------------')
print(df['A'].fillna(value=df['C'].mean()))
