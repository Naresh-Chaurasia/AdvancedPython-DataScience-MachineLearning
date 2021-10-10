try:
    a = [10, 20, 30]
    print(a[5])

    with open('pi_digits1.txt') as f:
        lines = f.read()
        print(lines)
except FileNotFoundError as e1:
    print('2')
    print(e1)
    print(type(e1))
except IndexError as e2:
    print('3')
    print(e2)
    print(type(e2))
except Exception as e3:
    print('1')
    print(e3)