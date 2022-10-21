from dataclasses import dataclass
import uuid
import os
import json
from xmlrpc.client import boolean


class Beardb:
    

    
    def __init__(self,project):
        if(os.path.exists(project)):
            self.project=project
        else:
            os.mkdir(project)
            
            self.project=project
        
        self.database:str =''
        self.database_active:boolean=False
        pass
    def path_(self,path):
        return os.path.join(self.project,path)
    # Create a new Database object.
    def create_database(self,database='') :
    
        if(os.path.exists(self.path_(database))):
            raise Exception(f'Database [{database}] already exists')
        else:
            
            os.mkdir(self.path_(database))
            self.database = database
            self.database_active=True
            
            
    # Load a database object.
    def load_database(self,database='') :
    
        if(os.path.exists(database)):
            self.database = database
            self.database_active=True
        else:
            raise Exception(f'Database [{database}] not found')
    
    # Load a database bucket
    
    def create_bucket(self,bucket_name=''):
        if(self.database_active):
            if(bucket_name==''):
                raise Exception('Bucket name is required')
     
              
            else: 
              path=self.path_(self.database+'/'+bucket_name)+'.json'
            
              with open(f'{path}', 'w') as outfile:
                    json.dump([], outfile)
           
        else:raise Exception('No database loaded')
    
   
    def fetchbyID(self,bucket_name='',id=''):   
        if(self.database_active):
            if(bucket_name==''):
                raise Exception('Bucket name is required')
            else:
                path=self.database+'/'+bucket_name+'.json'
                with open(path) as json_file:
                    data_list = json.load(json_file)
                    for data in data_list:
                        if(data['id']==id):
                            return data
                    return None
    def fetchData(self,bucket_name='',query={}):
        if(self.database_active):
            if(bucket_name==''):
                raise Exception('Bucket name is required')
            else:
                path=self.database+'/'+bucket_name+'.json'
                box  =[]
                with open(path) as json_file:
                    data_list = json.load(json_file)
                for data in data_list:
                    _ = 0
                    for key,value in query.items():
                       
                            if data[key]==value:
                                _+=1
                    if _ == len(query.items()):
                        box.append(data)
                                
                return box
        
        
        else:raise Exception('No database loaded')
    
    
    def updateData(self,bucket_name='',id='',data={}):
        if(self.database_active):
            if(bucket_name==''):
                raise Exception('Bucket name is required')
            else:
                path=self.database+'/'+bucket_name+'.json'
                with open(path) as json_file:
                    data_list = json.load(json_file)
                    for data in data_list:
                        if(data['id']==id):
                            for key,value in data.items():
                                if key in data:
                                 
                                    data[key]=value
                            break
                    with open(path, 'w') as outfile:
                        json.dump(data_list, outfile)
        
        else:raise Exception('No database loaded')

class Bucket:
    def __init__(self,project:object,bucket_name=''):
        
        self.project = project
        self.project_name=self.project.project
        self.database = self.project.database
        self.bucket_name=bucket_name
        self.database_active =False
        if(self.database!=''):
            self.database_active=True
        if(self.bucket_name==''):
                raise Exception('Bucket name is required')
        else:
            self.bucket_name = bucket_name.strip('')
        if(os.path.exists(self.path_(self.database+'/'+self.bucket_name+'.json'))):
 
            with open(self.path_(self.database+'/'+self.bucket_name+'.json')) as _:
                self.bucket = json.load(_)
        else:
            with open(self.path_(self.database+'/'+self.bucket_name+'.json'),'w') as __:
                json.dump([{}],__)
    def insert(self,data:dict={}):
        if(self.database_active):
            if(self.bucket_name==''):
                raise Exception('Bucket name is required')
            else:
             
                with open(self.path_(self.database+'/'+self.bucket_name+'.json')) as json_file:
                    data_list = json.load(json_file)
                    data['id']=str(uuid.uuid1())
                    data_list.append(data)
                    with open(self.path_(self.database+'/'+self.bucket_name+'.json'),'w') as outfile:
                        json.dump(data_list, outfile)
                
    def path_(self,path):
        return os.path.join(self.project_name,path)
    def fetchManybyId(self,id:list=[]):
        """
        id:int 
        Fetch data by id
        """
        if(self.database_active):
            if(self.bucket_name==''):
                raise Exception('Bucket name is required')
            else:
                path=self.path_(self.database+'/'+self.bucket_name+'.json')
                box  =[]
                with open(path) as json_file:
                    data_list = json.load(json_file)
                for data in data_list:
                    for i in id:
                        if data['id']==i:
                            box.append(data)
                return box
        else:raise Exception('No database loaded')
        
    def update(self,query:dict={},data:dict={}):
        if(self.database_active):
            if(self.bucket_name==''):
                raise Exception('Bucket name is required')
            else:
                path=self.path_(self.database+'/'+self.bucket_name+'.json')
                with open(path) as json_file:
                    data_list = json.load(json_file)
                    for data in data_list:
                        _ = 0
                        for key,value in query.items():
                            if data[key]==value:
                                _+=1
                        if _ == len(query.items()):
                            for key,value in data.items():
                                if key in data:
                                    data[key]=value
                    with open(path, 'w') as outfile:
                        json.dump(data_list, outfile)
        
        else:raise Exception('No database loaded')
    
   
    def updatebyId(self,id:str='',data:dict={}):
        if(self.database_active):
            if(self.bucket_name==''):
                raise Exception('Bucket name is required')
            else:
                path=self.path_(self.database+'/'+self.bucket_name+'.json')
                with open(path) as json_file:
                    data_list = json.load(json_file)
                    for data in data_list:
                        if(data['id']==id):
                            for key,value in data.items():
                                if key in data:
                                 
                                    data[key]=value
                            break
                    with open(path, 'w') as outfile:
                        json.dump(data_list, outfile)
        
        else:raise Exception('No database loaded')
    
    def delete(self,query:dict={}):
        if(self.database_active):
            if(self.bucket_name==''):
                raise Exception('Bucket name is required')
            else:
                path=self.path_(self.database+'/'+self.bucket_name+'.json')
                with open(path) as json_file:
                    data_list = json.load(json_file)
                    for data in data_list:
                        _ = 0
                        for key,value in query.items():
                            if data[key]==value:
                                _+=1
                        if _ == len(query.items()):
                            data_list.remove(data)
                    with open(path, 'w') as outfile:
                        json.dump(data_list, outfile)
        
        else:raise Exception('No database loaded')
        
    def deletebyId(self,id:str=''):
        if(self.database_active):
            if(self.bucket_name==''):
                raise Exception('Bucket name is required')
            else:
                path=self.path_(self.database+'/'+self.bucket_name+'.json')
                with open(path) as json_file:
                    data_list = json.load(json_file)
                    for data in data_list:
                        if(data['id']==id):
                            data_list.remove(data)
                            break
                    with open(path, 'w') as outfile:
                        json.dump(data_list, outfile)
        
        else:raise Exception('No database loaded')
    def fetchbyID(self,id:str=''):
        if(self.database_active):
            if(self.bucket_name==''):
                raise Exception('Bucket name is required')
            else:
                path=self.path_(self.database+'/'+self.bucket_name+'.json')
                with open(self.path_(self.database+'/'+self.bucket_name+'.json')) as json_file:
                    data_list = json.load(json_file)
                    for data in data_list:
                        if(data['id']==id):
                            return data
                    return None
    def fetchData(self,query:dict={}):
        if(self.database_active):
            if(self.bucket_name==''):
                raise Exception('Bucket name is required')
            else:
                path=self.database+'/'+self.bucket_name+'.json'
                box  =[]
                with open(self.path_(self.database+'/'+self.bucket_name+'.json')) as json_file:
                    data_list = json.load(json_file)
                for data in data_list:
                    _ = 0
                    for key,value in query.items():
                       
                            if data[key]==value:
                                _+=1
                    if _ == len(query.items()):
                        box.append(data)
                                
                return box
        
        
        else:raise Exception('No database loaded')
        
        

data = Beardb('server')
data.load_database('users')
newjson = Bucket(project=data,bucket_name='users')
newjson.insert(data={'name':'john','age':20})




# data.load_database('databasse')
# # data.insert_data(bucket_name='users1',data={'name':'david','age':420})
# print(data.fetchData(bucket_name='users1',query={"name": "david", "age": 421}))

