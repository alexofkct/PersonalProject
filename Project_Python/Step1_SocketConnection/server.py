import socket

#Variables
port=4444

s=socket.socket()
print("[+] Socket creation is successful")


s.bind(('',port))
print("[+] Socket binded to the port ",port)

s.listen(5)
print("[+] Open to connect and coffee chats")


while True:
	c, addr=s.accept()
	print("[+] Connection established from ",addr)
	c.send('Connection establishment successful\n'.encode())
	print(c.getpeername())
	print(c.getsockname())
	c.close()
	break

s.close()
