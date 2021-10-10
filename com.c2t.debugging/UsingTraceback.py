import traceback

def getError():
    v = 10/0

try:
    getError()
except:
    file = open('error.txt','w')
    file.write(traceback.format_exc())
    file.close()
    print('done.')