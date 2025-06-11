import socket, threading
from Crypto.Cipher import AES
import base64
import sys
import mysql.connector


#Functions
def sanitizer(str):
	str=str.split(" ")
	return str[1]

def reader(file):
        f=open(file,'r')
        var=f.read()
        return var.strip()

def pad(data):
	padding_length=16-(len(data)%16)
	padding=bytes([padding_length]*padding_length)
	return data.encode() + padding

def unpad(data):
    padding_length = data[-1]
    if padding_length < 1 or padding_length > 16:
        raise ValueError("Invalid padding encountered")
    return data[:-padding_length].decode()

def encryptor(msg):
        obj=AES.new(key,AES.MODE_CBC,IV)
        return obj.encrypt(pad(msg))

def decryptor(cipher):
        obj=AES.new(key,AES.MODE_CBC,IV)
        return unpad(obj.decrypt(cipher))

def sender(c: socket.socket):
	breaker=0
	while(breaker==0):
		helper=threading.Thread(target=receiver,args=[c])
		helper.daemon=True
		helper.start()
		msg=input()
		if(msg=="END"):
			breaker=1
		else:
			msg=str("Server: "+msg)
			c.send(encryptor(msg))

def receiver(c: socket.socket):
	while True:
		msg=decryptor(c.recv(1024))
		if(msg):
			print(msg)
			#broadcaster(c,msg)
'''def broadcaster(sender: socket.socket, msg: str):
	for connection in connections:
		if(connection!=sender):
			try:
				connection.send(encryptor(msg))
				print("Broadcast done!!!")
			except:
				connection_ender(connection)
				print(connection," session has died")

def connection_ender(conn: socket):
        conn.close()
        connections.remove(conn)
'''
def register(c: socket.socket):
	c.send(encryptor("Enter username:"))
	username=sanitizer(decryptor(c.recv(1024)))
	c.send(encryptor("Enter password:"))
	password=sanitizer(decryptor(c.recv(1024)))
	query="INSERT INTO user(username,password) VALUES (\'{0}\',\'{1}\');".format(username, password)
	try:
		cursor.execute(query)
		c.send(encryptor("[+] User registration is successful\nIt's time to login\nEnter username:"))
	except:
		c.send(encryptor("Username already exists"))
		c.close()
	db.commit()
	login(c)

def login(c: socket.socket):
	username=sanitizer(decryptor(c.recv(1024)))
	c.send(encryptor("Enter password:"))
	password=sanitizer(decryptor(c.recv(1024)))
	query="SELECT password FROM user WHERE username=\'"+username+"\';"
	cursor.execute(query)
	myresult=cursor.fetchall()
	if(myresult):
		if(password==myresult[0][0]):
			c.send(encryptor("[+] Welcome back,"+username+"\nAuthentication successful\nNow you can send or receive messages\n"))
			sender(c)
		else:
			c.send(encryptor("[-] Wrong password"))
			c.close()
	else:
		c.send(encryptor("[-] Wrong username"))
		c.close()

#Variables and initializations
port=4444
IP='127.0.0.1'
connections=[]
key = base64.b64decode(reader('/home/dev/Desktop/Project_Python/Step5_EncryptedChatRoom/private/key'))
IV = base64.b64decode(reader('/home/dev/Desktop/Project_Python/Step5_EncryptedChatRoom/private/IV'))
db=mysql.connector.connect(host="localhost",user="dev",password="password123",database="company")
cursor=db.cursor()
#Main function/code
try:
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((IP,port))
	s.listen(5)
	print("[+] The server is up and running...")
	while(True):
		c,addr=s.accept()
		print(addr, " connected")
		c.send(encryptor("Press the number of the operation you\'d like to do\n1.User registration\n2.User login"))
		option=int(sanitizer(decryptor(c.recv(1024))))
		if(option==1):
			register(c)
		if(option==2):
			c.send(encryptor("\nIt's time to login\nEnter username:"))
			login(c)
			'''
			print("First line of auth=True")
			connections.append(c)
			helper=threading.Thread(target=receiver,args=[c])
			helper.daemon=True
			helper.start()'''
except Exception as e:
	print("Encountered the following error",e)
finally:
	'''if(len(connections)>0):
		for conn in connections:
			connection_ender(conn)'''

s.close()
sys.exit()
