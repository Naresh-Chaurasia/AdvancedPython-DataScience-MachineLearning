import re

patternObject = re.compile('\d')
print(patternObject.findall('year 2017 is long gone. We are in 2018 and heading towards 2019'))

patternObjectPlus = re.compile('\d+')
print(patternObjectPlus.findall('year 2017 is long gone. We are in 2018 and heading towards 2019'))