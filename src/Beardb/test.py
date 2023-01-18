from Beardb import *
from Bucket import *


project = Beardb('random_project')
project.load_database('class') 

randomshit = Bucket(project,'randomshit')
print(randomshit.fetchData({}))
randomshit.updatebyId('b4e57d98-93c2-11ed-b0d6-324d38bf6d76',{'age:': 20})
print(randomshit.fetchData({}))