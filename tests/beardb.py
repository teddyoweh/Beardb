from dataclasses import dataclass
from tkinter import ON
import uuid
import os
import json
from xmlrpc.client import boolean


class Beardb:
    

    """
        Beardb is a simple local system database that uses json files to store data.
        
        
    """
    def __init__(self,project:str):
        """
        

        Args:
            project (str): _description_
        """
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
 
            
    # Load a database object.
    def load_database(self,database:str='test') :
        """
            Load a database object.

        Args:
            database (str, optional): _description_. Defaults to test.
        """
        
        if(os.path.exists(self.path_(database))):
            self.database = database
            self.database_active=True
        else:
            
            os.mkdir(self.path_(database))
            self.database = database
            self.database_active=True
         
    # Load a database bucket
    
 
class Bucket:
    """
        Buckets are the individual database files..

    """
    def __init__(self,project:object,bucket_name:str=''):
        """ 
 Buckets are the individual database files..
        Args:
            project (object): _description_
            bucket_name (str, optional): _description_. Defaults to ''.

        Raises:
            Exception: _description_
        """
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
                json.dump([],__)
    def insert(self,data:dict={}):
        """
        
            Insert data into a bucket 

        Args:
            data (dict, optional): _description_. Defaults to {}.

        Raises:
            Exception: _description_
        """
        
        if(self.database_active):
            if(self.bucket_name==''):
                raise Exception('Bucket name is required')
            else:
             
                with open(self.path_(self.database+'/'+self.bucket_name+'.json')) as json_file:
                
                    data_list = json.load(json_file)
                    data['_ßid']=str(uuid.uuid1())
                    data_list.append(data)
                    with open(self.path_(self.database+'/'+self.bucket_name+'.json'),'w') as outfile:
                        json.dump(data_list, outfile)
                
    def path_(self,path):
        return os.path.join(self.project_name,path)
    def fetchManybyId(self,id:list=[]):
        """
        
            Fetch many data by id stored in a list

        Args:
            id (list, optional): _description_. Defaults to [].

        Raises:
            Exception: _description_
            Exception: _description_

        Returns:
            _type_: _description_
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
        
    def fetchOne(self,query:dict={}):
        """_summary_

        Args:
            query (dict, optional): _description_. Defaults to {}.

        Raises:
            Exception: _description_
            Exception: _description_

        Returns:
            _type_: dict {data}
        """
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
                            return data
        else:raise Exception('No database loaded')

        

        
    def update(self,query:dict={},data:dict={}):
        """
                Update data in a bucket based on a query \n
                eg:\n
                ```
                query = {'name':'john','age':13}
                ```
               ``` 
               data = {'name':'john','age':20}
               ```
               ```
               update(query,data)
               ```     
          

        Args:
            query (dict, optional): _description_. Defaults to {}.
            data (dict, optional): _description_. Defaults to {}.

        Raises:
            Exception: Database not loaded
     
        """
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
        """
        
            Update data in a bucket based on an id

        Args:
            id (str, optional): _description_. Defaults to ''.
            data (dict, optional): _description_. Defaults to {}.

        Raises:
            Exception: _description_
            Exception: _description_
        """
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
        """
        
        Delete data in a bucket based on a query \n

        Args:
            query (dict, optional): _description_. Defaults to {}.

      """
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
        """
        Delete data in a bucket by id

        Args:
            id (str): _description_. Defaults to ''.
        Returns:
            _type_: _description_
        """

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
        
        """
        Fetch data in a bucket by id

        Args:
            id (str): _description_. Defaults to ''.
        Returns:
            _type_: _description_
        """
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
        """
        
        Fetch data based on a query

        Args:
            query (dict, optional): _description_. Defaults to {}.

 

        Returns:
            _type_: list [data]
        """
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

        
