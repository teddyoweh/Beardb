from Beardb import Beardb
from Bucket import Bucket
data = Beardb('testdb')
data.load_database('windowsapp')
newjson = Bucket(project=data,bucket_name='people')
newjson.insert(data={'name':'lucas','amountpaid':500,'email':'tedz@gmail.com'})


