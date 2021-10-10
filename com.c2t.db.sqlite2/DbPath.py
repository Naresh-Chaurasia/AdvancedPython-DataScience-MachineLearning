import sqlite3 as lite
 
con = lite.connect('user.db')

cur = con.cursor()
cur.execute("PRAGMA database_list")
rows = cur.fetchall()

for row in rows:
    print( row[0], row[1], row[2])