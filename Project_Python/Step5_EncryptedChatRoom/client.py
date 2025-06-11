import socket,threading
from Crypto.Cipher import AES
import base64
import sys
#Functions
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

def receiver(c: socket.socket):
	r_msg=c.recv(1024)
	if(r_msg):
		print(decryptor(r_msg))
#Initializations
key = base64.b64decode(reader('/home/dev/Desktop/Project_Python/EncryptedChatRoom/private/key'))
IV = base64.b64decode(reader('/home/dev/Desktop/Project_Python/EncryptedChatRoom/private/IV'))
port=4444
IP='127.0.0.1'
breaker=0
#Main function/code
try:
	c=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	c.connect((IP,port))
	while(breaker==0):
		helper=threading.Thread(target=receiver,args=[c])
		helper.daemon=True
		helper.start()
		msg=input()
		if(msg=="END"):
			breaker=1
		else:
			msg=str(c.getsockname()[0])+":"+str(c.getsockname()[1])+" "+msg
			c.send(encryptor(msg))
	c.close()
except Exception as e: 
	print("Entered the following error ",e)
print("Connection ended")
sys.exit()
