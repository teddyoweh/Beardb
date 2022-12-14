# Beardb
Database system implementing encrypted versions JSON of data. Easy to access, manage and deploy remotely

 ## Database Architecture
 
 ```
 -- Project
 | -- Database
 |    -- Bucket
 |      -- Data ({})
 ```

### Install Libraries
```sh
$ python3 -m pip install Beardb
```

#### Import Libraries
```py
from Beardb.Beardb import Beardb
from Beardb.Bucket import Bucket
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

### Test Code
```py
beardb_ = Beardb('projects')
beardb_.load_database('computers')
computers=Bucket(beardb_,'computers')
computers.insert({'model':'lenovo','ram':'8gb','hdd':'1tb','processor':'i5'})


```

License
----

MIT License

Copyright (c) 2022 Teddy Oweh

`teddyoweh built it`
