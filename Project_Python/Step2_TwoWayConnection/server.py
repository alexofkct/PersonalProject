import socket

#Variables
port=4444
breaker=0

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('',port))

s.listen(5)
c,addr=s.accept()

while(breaker!=1):
	msg=input("Me:")
	c.send(msg.encode())
	r_msg=c.recv(1024).decode()
	print("Client: ",r_msg)
	if((msg=="End") or (r_msg=="End")):
		breaker=1
c.close()
s.close()
