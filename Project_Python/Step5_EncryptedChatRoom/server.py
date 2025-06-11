import socket, threading
from Crypto.Cipher import AES
import sys
#Variables
port=4444
IP='127.0.0.1'
connections=[]

#Functions
def receiver(c: socket.socket):
	while True:
		msg=c.recv(1024)
		if(msg):
			print(msg)
			broadcaster(c,msg)
def broadcaster(sender: socket.socket, msg: str):
	for connection in connections:
		if(connection!=sender):
			try:
				connection.send(msg)
			except:
				connection_ender(connection)
				print(connection," session has died")

def connection_ender(conn: socket):
        conn.close()
        connections.remove(conn)

#Main function/code
try:
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((IP,port))
	s.listen(5)
	print("[+] The server is up and running...")
	while(True):
		c,addr=s.accept()
		print(addr, " connected")
		connections.append(c)
		helper=threading.Thread(target=receiver,args=[c])
		helper.daemon=True
		helper.start()
except Exception as e:
	print("Encountered the following error",e)
finally:
	if(len(connections)>0):
		for conn in connections:
			connection_ender(conn)

s.close()
sys.exit()
