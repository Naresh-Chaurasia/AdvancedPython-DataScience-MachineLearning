import numpy as np

#zeros
np_zeros = np.zeros(5)
print('np_zeros=',np_zeros)

print('np_zeros[1]=',type(np_zeros[1]))

np_zeros_2d = np.zeros((5,5))
print('np_zeros_2d=',np_zeros_2d)

np_zeros_int_1d = np.zeros((5), dtype=int)
print('np_zeros_int_1d=',np_zeros_int_1d)

np_zeros_int_2d = np.zeros((5,5), dtype=int)
print('np_zeros_int_2d=',np_zeros_int_2d)