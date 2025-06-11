import mysql.connector

#DB_Connection
db=mysql.connector.connect(host="localhost",user="dev",password="password123",database="company")
cursor=db.cursor()

def register():
	username=input("Enter username:")
	password=input("Enter password:")
	query="INSERT INTO user(username,password) VALUES (\'{0}\',\'{1}\');".format(username, password)
	try:
		cursor.execute(query)
		print("[+] User registration is successful")
	except:
		print("Username already exists")
		return 0
	db.commit()
	myresult=cursor.fetchall()
	for i in myresult:
		print(i[0])
	login()

def login():
	print("\nIt's time to login")
	username=input("Enter username:")
	password=input("Enter password:")
	query="SELECT password FROM user WHERE username=\'"+username+"\';"
	cursor.execute(query)
	myresult=cursor.fetchall()
	if(myresult):
		if(password==myresult[0][0]):
			print("[+] Welcome back,",username)
		else:
			print("[-] Wrong password")
	else:
		print("[-] Wrong username")

print("Press the number of the operation you\'d like to do")
print("1.User registration\n2.User login")
option=int(input())
if(option==1):
	register()
if(option==2):
	login()
