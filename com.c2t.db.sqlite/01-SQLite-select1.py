import sqlite3

conn = sqlite3.connect('edureka1.db')
print('connection established successfully...')

cursor1 = conn.cursor()

cursor1.execute("select * from stocks")
print('exection done...')
print(cursor1.fetchone())


conn.close()