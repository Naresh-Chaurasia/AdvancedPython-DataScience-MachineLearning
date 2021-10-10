import os
import os.path

the_path='D:/nchaurasia/Python-Architect/connect2tech.in-Python/abs_al_sweigart'
the_list = os.listdir(the_path)
print(the_list)

print('------------------------------------')

for i in (os.listdir('D:/nchaurasia/Python-Architect/connect2tech.in-Python/abs_al_sweigart')):

    if os.path.isdir(the_path + '/'+ i):
        print('Directory Name i=',i)
    else:
        print("Files List i=" , i)
