import numpy as np

# 2D
array_2d = [[1,2,3,4,5],
            [10,20,30,40,50],
            [100,200,300,400,500]
            ] # Creating two dimensional array


np_array_2d = np.array(array_2d)

print(np_array_2d)

print(np_array_2d[0,0])
print(np_array_2d[0][0])
print(np_array_2d[:2])
print(np_array_2d[:])
print(np_array_2d[1:])
print('----------------')
#print(np_array_2d[2:][:2])

