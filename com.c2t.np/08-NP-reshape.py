import numpy as np

# 1D
array_1d = [1,2,3,4,5,6]
print('array_1d:',array_1d)

np_array_1d = np.array(array_1d)
print('np_array_1d:',np_array_1d)
print('np_array_1d.shape:',np_array_1d.shape)

print('np_array_1d.reshape(2,3)=',np_array_1d.reshape(2,3))
print('np_array_1d.reshape(2,3).shape=',np_array_1d.reshape(2,3).shape)

