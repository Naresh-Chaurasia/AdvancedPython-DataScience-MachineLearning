import numpy as np

np_arr = np.arange(0,11)
print('np_arr =',np_arr)

#Broadcasting
np_arr[0:2] = 100
print('np_arr =',np_arr)


np_arr2 = np.arange(0,11)
slice_np_arr2 = np_arr2[0:2]
print('slice_np_arr2=',slice_np_arr2)
slice_np_arr2[:] = 200
print('slice_np_arr2=',slice_np_arr2)
print('np_arr2=',np_arr2)