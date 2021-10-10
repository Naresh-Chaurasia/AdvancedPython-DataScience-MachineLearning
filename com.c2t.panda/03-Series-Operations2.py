import pandas as pd
import numpy as np

arr1 = [10,20,30]
labels1 = ['a','b','c']

arr2 = [10,20,30]
labels2 = ['a','b','d']

series1 = pd.Series(arr1,labels1)
#print(series1)
print('-------------------------------')
series2 = pd.Series(arr2, labels2)
#print(series2)

print('-------------------------------')
ser3 = series1 + series2
print(ser3)
