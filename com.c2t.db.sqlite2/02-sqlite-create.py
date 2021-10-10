import sqlite3

conn = sqlite3.connect('edureka.db')
cursor = conn.cursor()
print("Opened database successfully")

cursor.execute('drop table company')

cursor.execute('''CREATE TABLE COMPANY
         (ID INT ,
         NAME           TEXT    ,
         AGE            INT     ,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
print("Table created successfully")

conn.close()