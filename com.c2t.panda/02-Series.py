import pandas as pd
import numpy as np


arr = [10,20,30]
labels = ['a','b','a']
np_arr = np.array(arr)
dict = {'a':10,'b':20}

ser1 = pd.Series(data=arr,index=labels)

#print(ser1['a'])

print(pd.Series(dict))