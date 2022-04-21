import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                                 user='root',
                                 passwd='shafita77',
                                 )

cursor = mydb.cursor()
#cursor.execute("CREATE DATABASE stock")
cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)