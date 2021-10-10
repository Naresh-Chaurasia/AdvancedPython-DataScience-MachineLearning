import sqlite3

conn = sqlite3.connect('python.db')
print('connection established')

cursor = conn.cursor()

# Insert a row of data
cursor.execute("update stocks set qty = ? where symbol = ? ",(120,'RHAT'))

conn.commit()
conn.close()
print('Record inserted in table.')