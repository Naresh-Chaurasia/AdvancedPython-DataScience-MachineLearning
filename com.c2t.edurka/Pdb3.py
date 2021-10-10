import pdb

def recursive_calls(i = 5, output = 'somethign here'):
    if i > 0:
        recursive_calls(i - 1)
    else:
        pdb.set_trace()
        print(output)
    return

if __name__ == '__main__':
    recursive_calls()