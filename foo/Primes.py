'''
Created on 17-Apr-2018

@author: naresh
'''


def is_prime(number):
    """Return True if *number* is prime."""
    for element in range(2,number):
        print('element=',element)
        mod = number % element
        print('mod=',mod)
        if mod == 0:
            return False

    return True


def print_next_prime(number):
    """Print the closest prime number larger than *number*."""
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)
