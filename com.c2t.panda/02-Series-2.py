import pandas as pd
import numpy as np



labels = ['a','b','a']

ser1 = pd.Series(data=[sum,print,len],index=labels)

print(ser1)