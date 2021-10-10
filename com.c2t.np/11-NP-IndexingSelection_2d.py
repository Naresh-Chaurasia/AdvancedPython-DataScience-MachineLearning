import numpy as np

# 2D
array_2d = [[1,2,3,4,5],
            [10,20,30,40,50],
            [100,200,300,400,500]
            ] # Creating two dimensional array
print('array_2d:',array_2d)
np_array_2d = np.array(array_2d) # Creating NumPy two dimensional array
print('np_array_2d:',np_array_2d)
print('type(np_array_2d):',type(np_array_2d))

print('np_array_2d[:2,2:] =',np_array_2d[:2,2:])
print('np_array_2d[:2] =',np_array_2d[:2])