import numpy as np

np_arr = np.arange(0,11)
print('np_arr =',np_arr)

comparison_arr = np_arr > 5

print(comparison_arr)
print(np_arr[comparison_arr])
print(np_arr[np_arr > 5])