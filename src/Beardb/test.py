from Beardb import Beardb
from Bucket import Bucket
data = Beardb('testdb')
data.load_database('windowsapp')
newjson = Bucket(project=data,bucket_name='people')
newjson.insert(data={"name":"teddyclear","amountpaid":400,"email":"tedz@gmail.com"})
# print(newjson.fetchData())
# import json
# name = '{"name":"lucas","amountpaid":500,"email}'

# names = json.loads
# print(names)\\
# from cryptography.fernet import Fernet
# print(Fernet.generate_key())

# open('key.key','wb').write(Fernet.generate_key())