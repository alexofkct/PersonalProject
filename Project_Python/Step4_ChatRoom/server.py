import socket, threading
#Variables
port=4444
connections=[]

#Functions
def receiver(c: socket.socket):
	while True:
		msg=c.recv(1024)
		if(msg):
			final_msg=' '.join(str(val) for val in c.getpeername())
			final_msg+=" : "+msg.decode()
			print(final_msg)
			broadcaster(c,final_msg)
def broadcaster(sender: socket.socket, msg: str):
	for connection in connections:
		if(connection!=sender):
			try:
				connection.send(msg.encode())
			except:
				connection_ender(connection)
				print(connection," session has died")

def connection_ender(conn: socket):
        conn.close()
        connections.remove(conn)

try:
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('',port))
	s.listen(5)
	print("[+] The server is up and running...")
	while(True):
		c,addr=s.accept()
		print(addr, " connected")
		c.send('THIS IS YOUR CAPTAIN SPEAKING...'.encode())
		connections.append(c)
		threading.Thread(target=receiver,args=[c]).start()
except Exception as e:
	print("Encountered the following error",e)
finally:
	if(len(connections)>0):
		for conn in connections:
			connection_ender(conn)

s.close()
