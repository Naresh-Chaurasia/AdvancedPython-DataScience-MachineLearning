balance = input('enter your balance amount')

try:
    if int(balance) > 500:
        print('you can withdraw money...')
    else:
        raise RuntimeError('You have insufficient balance...')
except RuntimeError as run:
    print(run)
