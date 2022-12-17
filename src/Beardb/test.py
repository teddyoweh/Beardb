from Beardb import Beardb
from Bucket import Bucket
from Client import Client

data = Beardb('sodd')
data.load_database('windowsapp')
newjson = Bucket(project=data,bucket_name='people')
# newjson.schemas(
#     {
#        'type':str,
#        'id':int,
#        'name':str,
#        'email':str,
#        'list':list

#     }
# )
newjson.insert(data={"name":"oweh","amountpaid":400,"email":"tedz@gmail.com"})
# newjson.update(query={'email': 'tedz@gmail.com'},data={'name':'amaka done blow'})
# newjson.updatebyId(id='48b27e8c-7db5-11ed-9e76-324d38bf6d76',data={"name":"james","amountpaid":1555500})
print(newjson.fetchData())
# import json
# name = '{"name":"lucas","amountpaid":500,"email}'

# names = json.loads
# print(names)\\
# from cryptography.fernet import Fernet
# print(Fernet.generate_key())

# open('key.key','wb').write(Fernet.generate_key())