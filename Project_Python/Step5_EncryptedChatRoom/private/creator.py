import os
import base64


key = os.urandom(32)
iv = os.urandom(16)

key_encoded=base64.b64encode(key).decode()
iv_encoded=base64.b64encode(iv).decode()

with open('key','w') as f:
	f.write(key_encoded)
	f.close()
with open('IV','w') as f:
	f.write(iv_encoded)
	f.close()

print("[+] Key and IV are created and stored in separate files...")
