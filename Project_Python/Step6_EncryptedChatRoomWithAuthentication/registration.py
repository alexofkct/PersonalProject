import mysql.connector

db=mysql.connector.connect(host="localhost",user="dev",password="password123",database="company")
cursor=db.cursor()

username=input("Enter username:")
password=input("Enter password:")
query="INSERT INTO user(username,password) VALUES (\'{0}\',\'{1}\');".format(username, password)
print(query)

cursor.execute(query)
print("[+] User registration is successful")
query="SELECT * FROM user;"
cursor.execute(query)
myresult=cursor.fetchall()

for i in myresult:
	print(i)
