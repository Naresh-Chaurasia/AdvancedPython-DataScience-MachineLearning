import traceback


a = [1, 2, 3]
try: 
    print ("Second element = ",(a[1]))
 
    # Throws error since there are only 3 elements in array
    print ("Fourth element = ", (a[3])) 
 
except Exception as e:
    msg = traceback.format_exc()
    print(msg)
    f1 = open('msg.txt','w')
    f1.write(msg)
    f1.close()
    
