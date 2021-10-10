import sqlite3

con = sqlite3.connect('test.db')
cursor = con.cursor()

for row in cursor.execute('SELECT * FROM stocks ORDER BY price'):
   print(row)

