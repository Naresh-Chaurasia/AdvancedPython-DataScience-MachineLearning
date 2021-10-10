import sqlite3

#creating connection
conn = sqlite3.connect('edureka.db')
print('connection create successfully ->', conn)
print('connection create successfully ->', type(conn))

# Create cursor
cursor = conn.cursor()
print('cursor create successfully ->', cursor)
print('cursor create successfully ->', type(cursor))

# Create table

query = 'CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)'


