from Beardb import *
from Bucket import *


project = Beardb('random_project')
project.load_database('class') 

randomshit = Bucket(project,'randomshits')
# print(randomshit.fetchData({}))
 
print(randomshit.fetchData({}))
# randomshit.insert({
#     'name':'ted',
#     'age':43
# })

randomshit.updatebyId('555f6118-976e-11ed-b9a8-324d38bf6d76',{'age': 350})
print(randomshit.fetchData({}))


# org = {'name': 'teddy', 'age': 45, 'id': 'b4e57d98-93c2-11ed-b0d6-324d38bf6d76'}
# print(org)
# org.update({'age': 43})
# print(org)
