import mysql.connector

db=mysql.connector.connect(host="localhost",user="dev",password="password123",database="company")
cursor=db.cursor()

username=input("Enter username:")
password=input("Enter password:")
query="SELECT password FROM user WHERE username=\'"+username+"\';"

cursor.execute(query)
myresult=cursor.fetchall()


if(myresult):
	if(password==myresult[0][0]):
		print("[+] Welcome back,",username)
	else:
		print("[-] You are almost there. Give one more try for the password.")
else:
	print("[-] Seriously? You forgot your username?")

