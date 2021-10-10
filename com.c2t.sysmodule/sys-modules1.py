import sys
import os

cwd = os.getcwd()
mod = sys.modules.keys()
print('mod=',mod)
print('cwd=',cwd)


for m in mod:
    print('m=',m)

