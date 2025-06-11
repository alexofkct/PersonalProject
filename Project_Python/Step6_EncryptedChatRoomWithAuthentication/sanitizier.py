str="127.0.0.1:12345 1"
str2="127.0.0.1:12345 admin"

def sanitizier(str):
	str=str.split(" ")
	return str[1]

print(type(sanitizier(str)))
print(type(sanitizier(str2)))
