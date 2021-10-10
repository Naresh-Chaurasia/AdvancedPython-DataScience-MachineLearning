import sqlite3 as lite
import sys

con = None
 
try:
    con = lite.connect('test.db')
    cur = con.cursor()    
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()
    print ("SQLite version: %s",data )               
except BaseException:   
    print ('error')
    sys.exit(1)
finally:    
    if con:
        con.close()