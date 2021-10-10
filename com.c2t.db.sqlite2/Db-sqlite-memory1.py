import sqlite3

con = sqlite3.connect(':memory:')
cursor = con.cursor()

#cursor.execute('DROP TABLE stocks')
#print('dropped table')

cursor.execute('CREATE TABLE stocks(date text, trans text, symbol text, qty real, price real)')
print('create table')

cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT2',100,35.14)")
print('inserted data into table')

# Save (commit) the changes
con.commit()
print('commit done')

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
print('connection close')


con = sqlite3.connect(':memory:')
cursor = con.cursor()

for row in cursor.execute('SELECT * FROM stocks ORDER BY price'):
   print(row)