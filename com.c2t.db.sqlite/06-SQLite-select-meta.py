import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

# Do this instead
t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)


print('Chapter table has these columns:')
for column_info in c.description:
    print(column_info)


# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()