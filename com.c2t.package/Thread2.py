import threading, time

print('Let\' get started...')

def takeNap(a1):
    print('2. threading.current_thread() =', threading.current_thread())
    print('a1=',a1)
    time.sleep(5)
    print('I just got up...')

thread = threading.Thread(target=takeNap,args=('a'))
thread.start()
print('1. threading.current_thread() =',threading.current_thread())

print('I am done..')