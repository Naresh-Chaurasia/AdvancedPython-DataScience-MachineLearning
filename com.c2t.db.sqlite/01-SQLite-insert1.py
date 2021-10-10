import sqlite3

conn = sqlite3.connect('python.db')
print('connection established')

cursor = conn.cursor()

# Insert a row of data
cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

print('table created')
conn.commit()

conn.close()