try:
    '''with open('pi_digits1.txt') as f:
        lines = f.read()
        print(lines)
        '''
    a = [10,20,30]
    print(a[5])
except Exception as e:
    print('The file does not exist.')
    print(type(e))