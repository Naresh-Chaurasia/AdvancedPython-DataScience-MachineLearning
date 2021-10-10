import pandas as pd
import numpy as np


arr = [10,20,30]
labels = ['a','b','a']
np_arr = np.array(arr)

print(pd.Series())


#print(pd.Series(data=arr,index=labels))
'''
print(pd.Series(arr,index=labels))
print(pd.Series(arr,labels))

print('pd.Series(np_arr)=',pd.Series(np_arr),sep='\n')
print('pd.Series(dict)=',pd.Series(dict))

print('pd.Series(labels)=',pd.Series(labels))

#Reference to inbuilt functions
print('pd.Series(data=[sum, print, len])=',pd.Series(data=[sum, print, len]))
'''