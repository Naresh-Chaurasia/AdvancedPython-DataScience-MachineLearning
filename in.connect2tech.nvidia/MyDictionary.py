myDict = {"key1":"value1","user":"naresh"}

print('----------')
print(myDict['k1'])

print('----------')
for key in myDict:
    print(key)


dictComprehension={len(key):len(key) for key in myDict}
print('----------')
print(dictComprehension)