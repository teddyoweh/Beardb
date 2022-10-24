# Beardb
 A Local System Based JSON Database system 

### Install Libraries
```sh
$ pip install Beardb
```

#### Import Libraries
```py
from Beardb import Beardb, Bucket
```
#### Initialize Project
```py

project = Beardb('projectname')
project.load_database('class') 
```
#### Initialize Bucket(DataBase File)

```py
users = Bucket(project=project, bucket_name='users') # Project variable defined in the initialization 
```

#### Insert Data into Bucket
```py
data = {
       'name':'Teddy Oweh',
       'Random Data':'Golf'
}
users.insert(data=data})

"""
Output in database:
[
 {       
        'id':'ae0ca44e-5301-11ed-8d24-a6bd5a94b3a6',
        'name':'Teddy Oweh',
        'Random Data':'Golf'
 }
]

"""
```

#### Updata Data in Bucket From Query
```py
query= {
       'name':'Teddy Oweh',
       'Random Data':'Golf'
}
newdata = {
       'name':'Teddy Oweh',
       'Random Data':'Ping Pong',
       'Added Data':'College'
       
}

users.update(query=query,data=newdata})

"""
Old Output in database:
[
 {       
        'id':'ae0ca44e-5301-11ed-8d24-a6bd5a94b3a6',
        'name':'Teddy Oweh',
        'Random Data':'Golf'
 }
]
New Output in database:
[
 {       
        'id':'ae0ca44e-5301-11ed-8d24-a6bd5a94b3a6',
        'name':'Teddy Oweh',
        'Random Data':'Ping Pong',
        'Added Data':'College'
 }
]

"""
```

#### Update Data From Bucket From ID
```py
       'Random Data':'Golf'
}
newdata = {
       'name':'Teddy Oweh',
       'Random Data':'Ping Pong',
       'Added Data':'College'
       
}

users.updatebyId(id='ae0ca44e-5301-11ed-8d24-a6bd5a94b3a6',data=newdata})

"""
Old Output in database:
[
 {       
        'id':'ae0ca44e-5301-11ed-8d24-a6bd5a94b3a6',
        'name':'Teddy Oweh',
        'Random Data':'Golf'
 }
]
New Output in database:
[
 {       
        'id':'ae0ca44e-5301-11ed-8d24-a6bd5a94b3a6',
        'name':'Teddy Oweh',
        'Random Data':'Ping Pong',
        'Added Data':'College'
 }
]

"""
```

#### Delete Data From Bucket From Query

```py
query= {
       'name':'Teddy Oweh',
       'Random Data':'Golf'
}
 

users.delete(query=query})
 
```
#### Delete Data From Bucket From ID

```py

users.deletebyId(id="ae0ca44e-5301-11ed-8d24-a6bd5a94b3a6")
 
```

#### Fetch Data From ID
```py

userinfo = users.fetchbyID(id="ae0ca44e-5301-11ed-8d24-a6bd5a94b3a6")

```


#### Fetch Data From Query
```py
query= {
       'name':'Teddy Oweh',
       'Random Data':'Golf'
}
userinfo = users.fetchData(query=query)

```

