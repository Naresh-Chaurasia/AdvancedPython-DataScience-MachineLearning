import threading, time

def myThread():
    print('I am myThread')
    print('2.1. threading.current_thread()=', threading.current_thread())
    time.sleep(2)
    print('after sleep of 2 seconds')
    print('2.2. threading.current_thread()=', threading.current_thread())


thread = threading.Thread(target=myThread)
thread.start()
print('1. threading.current_thread()=',threading.current_thread())
