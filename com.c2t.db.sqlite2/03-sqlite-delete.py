import sqlite3

conn = sqlite3.connect('edureka.db')
print("Opened database successfully")

cursor2 = conn.cursor()
c2 = cursor2.execute("delete from company where ID = ?", (1,))
conn.commit

print(conn.total_changes)

conn.close()