import time, threading

def thread1():
    print('2. threading.current_thread()   :', threading.current_thread())
    print('I am a thread1')
    time.sleep(1)

'''
thread1()
thread2()
print('1. threading.current_thread()   :',threading.current_thread())
'''

t1 = threading.Thread(target=thread1)
t1.start()

print('1. threading.current_thread()   :',threading.current_thread())








'''
t1 = threading.Thread(target=thread1)
t1.start()

t2 = threading.Thread(target=thread2)
t2.start()

print('1. threading.current_thread()   :',threading.current_thread())
'''
