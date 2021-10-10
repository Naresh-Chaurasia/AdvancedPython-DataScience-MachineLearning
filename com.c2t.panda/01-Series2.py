import pandas as pd
import numpy as np


arr = [10,20,30]
labels = ['row1','row2','row3']

series1 = pd.Series(data=arr)

print(series1)
print(type(series1))

#print(series1['row1'])
print(series1[0])