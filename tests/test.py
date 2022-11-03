from Beardb.Beardb import Beardb
from Beardb.Bucket import Bucket
data = Beardb('testdb')
data.load_database('windowsapp')
newjson = Bucket(project=data,bucket_name='people')
newjson.insert(data={'name':'lucas','amountpaid':500,'email':'tedz@gmail.com'})




# beardb_ = Beardb('projects')
# beardb_.load_database('computers')
# computers=Bucket(beardb_,'computers')
# computers.insert({'model':'lenovo','ram':'8gb','hdd':'1tb','processor':'i5'})
# computers.insert({'model':'lenovo','ram':'8gb','hdd':'1tb','processor':'i5'})
# computers.insert({'model':'lenovo','ram':'8gb','hdd':'1tb','processor':'i5'})
# computers.insert({'model':'lenovo','ram':'8gb','hdd':'1tb','processor':'i5'})
# computers.insert({'model':'lenovo','ram':'8gb','hdd':'1tb','processor':'i5'})
# computers.insert({'model':'lenovo','ram':'8gb','hdd':'1tb','processor':'i5'})