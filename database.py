import mysql.connector as sql

## please use your personal sql password here
mycon = sql.connect(host="localhost",user="root",password="123456",auth_plugin = "mysql_native_password")
cursor = mycon.cursor()

cursor.execute("use megamarket")
cursor.execute("select* from product")
data = cursor.fetchall()
print(data)