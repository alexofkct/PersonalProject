import socket

port=4444
breaker=0
c=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c.connect(('',port))

while(breaker!=1):
	r_msg=c.recv(1024).decode()
	print("Server:",r_msg)
	msg=input("Me:")
	c.send(msg.encode())
	if((msg=="End") or r_msg=="End"):
		breaker=1
c.close()
