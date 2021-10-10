import sqlite3

conn = sqlite3.connect('python.db')
print('connection established')

cursor = conn.cursor()

# Insert a row of data
cursor.execute("INSERT INTO stocks VALUES (?,?,?,?,?)",('2006-01-06','BUY1','RHAT1',101,35.11))
print(cursor.lastrowid)
conn.commit()
conn.close()
print('Record inserted in table.')