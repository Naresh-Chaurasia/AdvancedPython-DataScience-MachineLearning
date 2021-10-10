import sqlite3

conn = sqlite3.connect('python.db')
print('connection established successfully...')

cursor1 = conn.cursor()

for row in cursor1.execute('select * from stocks'):
    print(row)

    for val in row:
        print(val)
        print(type(val))

conn.close()