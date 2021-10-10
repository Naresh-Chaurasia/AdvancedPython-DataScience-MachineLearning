import os

rootDir = 'D:/nchaurasia/Python-Architect/connect2tech.in-Python/abs_al_sweigart/'

dirs = os.listdir(rootDir)

for dir in dirs:
    print('dir=',dir)
    ch_dir = rootDir + dir
    print('ch_dir=',ch_dir)
    os.chdir(ch_dir)
    print(os.listdir('.'))
    os.chdir(rootDir)