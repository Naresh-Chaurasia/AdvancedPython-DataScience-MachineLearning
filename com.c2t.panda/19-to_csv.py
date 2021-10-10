import numpy as np
import pandas as pd

df = pd.read_csv('example')
print(df)

#df.to_csv('write-to-csv',index=False)
#df.to_csv('write-to-csv')

df.to_csv('write-to-csv.csv')

