import pandas as pd
import  numpy  as np
from numpy.random import randn

np.random.seed(101)

df3 = pd.DataFrame(randn(5,4),['r1','r2','r3','r4','r5'],['c1','c2','c3','c4'])
print('----------------df3-------------------')
print(df3)


# 1. First identify the column
# 2. Find the columns > 0
# 3. Display the content of frame as per column 2
c1_df3 = df3['c1']
print('----------------c1_df3-------------------')
print(c1_df3)

c1_df3_gt_0 = df3['c1'] > 0
print('---------------c1_df3_gt_0--------------------')
print(c1_df3_gt_0)

print('---------------df3[c1_df3_gt_0]--------------------')
print(df3[c1_df3_gt_0])

# Compare it with the following output below.
print('---------------df3[df3>0]--------------------')
print(df3[df3>0])


print('-----------------------------------')
print(df3[c1_df3_gt_0]['c2'])
print('-----------------------------------')
print(df3[c1_df3_gt_0][['c2','c2']])


#print(c1_df3>0)
#print(df3[c1_df3>0])
'''
print(df3[df3['c1']>0])
print(df3[df3['c1']>0]['c2'])
print(df3[df3['c1']>0][['c2','c1']])
'''

#More Memory
'''
bool_c1_condition = df3['c1']>0
print(bool_c1_condition)
df3_bool_c1_condition = df3[bool_c1_condition]
print(df3_bool_c1_condition)
df3_bool_c1_condition_columns = df3_bool_c1_condition['c1']
print(df3_bool_c1_condition_columns)
'''

