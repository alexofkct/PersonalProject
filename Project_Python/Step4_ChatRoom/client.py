import socket,threading

port=4444

def receiver(c: socket.socket):
	r_msg=c.recv(1024)
	if(r_msg):
		print(r_msg.decode())
try:
	c=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	c.connect(('',port))
	while(True):
		threading.Thread(target=receiver,args=[c]).start()
		msg=input()
		if(msg=="END"):
			break
		else:
			c.send(msg.encode())
	c.close()
except Exception as e: 
	print("Entered the following error ",e)
