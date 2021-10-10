import sqlite3

conn = sqlite3.connect('python.db')
print('connection established')

cursor = conn.cursor()

# Insert a row of data
data = {'date':'2006-01-06','var1':'BUY2','var2':'RHAT2','val1':102,'val2':12.8}
cursor.execute("INSERT INTO stocks VALUES (:date,:var1,:var2,:val1,:val2)",data)
conn.commit()
conn.close()
print('Record inserted in table.')