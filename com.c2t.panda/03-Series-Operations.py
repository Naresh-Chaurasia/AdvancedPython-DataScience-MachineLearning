import pandas as pd
import numpy as np

arr1 = [10,20,30]
labels1 = ['a','b','c']

arr2 = [10,20,30]
labels2 = ['a','b','c']

ser1 = pd.Series(data=arr1,index=labels1)
ser2 = pd.Series(data=arr2,index=labels2)

print(ser1)
print('-------------------------------')

print(ser2)
print('-------------------------------')

ser_sum = ser1 + ser2
print(ser_sum)
print('-------------------------------')

ser_mul = ser1 * ser2
print(ser_mul)
print('-------------------------------')

ser_div = ser1 / ser2
print(ser_div)
print('-------------------------------')