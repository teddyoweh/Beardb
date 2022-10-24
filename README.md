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



License
----

MIT License

Copyright (c) 2022 Teddy Oweh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

`teddyoweh built it`
