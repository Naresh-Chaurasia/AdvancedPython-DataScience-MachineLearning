import sqlite3

conn = sqlite3.connect('edureka.db')
print("Opened database successfully")

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
    print(row)

print("Operation done successfully")
conn.close()
