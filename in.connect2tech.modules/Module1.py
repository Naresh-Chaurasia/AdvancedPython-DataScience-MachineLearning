import sys

def mod1():
    print('I am in mod1')
    sys_path = sys.path
    
    for v in sys_path:
        print(v)