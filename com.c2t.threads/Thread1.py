import threading, time

def myThread():
    print('I am myThread')
    print('2.1. threading.current_thread()=', threading.current_thread())
    time.sleep(2)
    print('after sleep of 2 seconds')
    print('2.2. threading.current_thread()=', threading.current_thread())

def myThread2():
    print('I am myThread')
    print('3.1. threading.current_thread()=', threading.current_thread())
    time.sleep(2)
    print('after sleep of 2 seconds')
    print('3.2. threading.current_thread()=', threading.current_thread())


thread = threading.Thread(target=myThread)
thread.start()
print('1. threading.current_thread()=',threading.current_thread())

thread2 = threading.Thread(target=myThread2)
thread2.start()
print('1. threading.current_thread()=',threading.current_thread())