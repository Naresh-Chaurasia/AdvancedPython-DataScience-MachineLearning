import sqlite3
conn = sqlite3.connect('transaction.db')

c = conn.cursor()

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT-2',100,35.14)")

# Save (commit) the changes
# conn.commit()

conn2 = sqlite3.connect('transaction.db')
c2 = conn2.cursor()
c2.execute("SELECT * FROM stocks")
print('Select before commit...')
print(c2.fetchone())



# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()