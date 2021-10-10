str1 = 'hello how are you. I am fine. How are you'

spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".
Please do not drink it.
Sincerely,
Bob'''

print('str1.split()=',str1.split())

print("str1.split('are')=",str1.split('are'))

print("spam.split('\\n')=",spam.split('\n'))