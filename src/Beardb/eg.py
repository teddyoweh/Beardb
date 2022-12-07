from cryptography.fernet import Fernet
key = open('key.key','rb').read()
data = open('test.key','rb').read()
fernet =Fernet(key)
ans =fernet.decrypt(data).decode()
 
import json

vac = json.loads(json.dumps(ans))
print(vac[0])
#print(dict([{'name': 'lucas', 'amountpaid': 500, 'email': 'tedz@gmail.com', '_id': '3911d5a8-5eb7-11ed-8141-a6bd5a94b3a6'}]))
