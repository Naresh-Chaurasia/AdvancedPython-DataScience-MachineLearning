import sqlite3

conn = sqlite3.connect('sql.db')
print('connection established successfully...')

cursor1 = conn.cursor()

# Larger example that inserts many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]

cursor1.executemany('insert into stocks values(?,?,?,?,?)',purchases)
conn.commit()
conn.close()