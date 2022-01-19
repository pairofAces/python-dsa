# hypothetical example of connecting to a MySql database

import mysql.connector
con = mysql.connector.connect( host = "host", user = "username", 
    passwd = "password", database = "database")
cur = con.cursor()
cur.execute("INSERT INTO Computer VALUES (1005, 'Deli', 'Vostro', 2013)");
print(cur.rowcount)
cur.close()
con.commit()
con.close()