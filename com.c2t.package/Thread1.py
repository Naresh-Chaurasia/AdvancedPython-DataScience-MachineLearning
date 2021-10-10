import threading, time

print('Let\' get started...')

def takeNap():
    print('2. threading.current_thread() =', threading.current_thread())
    time.sleep(5)
    print('I just got up...')

thread = threading.Thread(target=takeNap)
thread.start()
print('1. threading.current_thread() =',threading.current_thread())

print('I am done..')