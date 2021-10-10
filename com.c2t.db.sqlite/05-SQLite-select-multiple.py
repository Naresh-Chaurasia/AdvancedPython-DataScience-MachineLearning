import sqlite3
conn = sqlite3.connect('python.db')

c = conn.cursor()

rows = c.execute('SELECT * FROM stocks ORDER BY price')

print(rows)

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()