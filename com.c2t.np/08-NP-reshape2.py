import numpy as np

# 1D
array_1d = [10,20,30,40,50,60]

np_1d = np.array(array_1d)
print(np_1d)

print('np_1d.shape=',np_1d.shape)

np_23 = np_1d.reshape(4,2)
print('np_23=',np_23)
print('np_23.shape=',np_23.shape)



