import mysql.connector


try:
    cnx = mysql.connector.connect(user='root', password='password',
                              host='localhost',
                              database='mydb1')
except Exception as err:
    print(err)
else:
    cnx.close()