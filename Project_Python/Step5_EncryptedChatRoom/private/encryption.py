from Crypto.Cipher import AES
import base64
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

key = base64.b64decode(reader('key'))
IV = base64.b64decode(reader('IV'))
msg="This is a sample sentence"

cipher=encryptor(msg)
print(cipher)
msg=decryptor(cipher)
print(msg)
