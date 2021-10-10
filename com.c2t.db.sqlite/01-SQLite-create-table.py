import sqlite3
conn = sqlite3.connect('edureka1.db')

c = conn.cursor()

# Create table
# c.execute('''DROP TABLE stocks''')

# Create table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()