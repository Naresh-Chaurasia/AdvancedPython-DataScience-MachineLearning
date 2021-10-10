import sqlite3
conn = sqlite3.connect('python.db')

c = conn.cursor()

# Never do this -- insecure!
symbol = 'RHAT'
c.execute("SELECT * FROM stocks WHERE symbol = 'RHAT'" )
print(c.fetchone())

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()