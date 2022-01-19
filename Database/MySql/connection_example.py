# hypothetical example of connecting to a MySql database
# ---------------------------------------------------------------------
    # Establish a connection to the database

import mysql.connector
con = mysql.connector.connect( host = "host", user = "username", 
    passwd = "password", database = "database")
# ---------------------------------------------------------------------
    # Execute a query

cur = con.cursor()
cur.execute("INSERT INTO Computer VALUES (1005, 'Deli', 'Vostro', 2013)");

# ---------------------------------------------------------------------
    # print the results of the query

print(cur.rowcount)
# ---------------------------------------------------------------------
    # clean up and close the connection
    
cur.close()
con.commit()
con.close()