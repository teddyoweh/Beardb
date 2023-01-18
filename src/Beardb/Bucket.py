import uuid
import os
import json
import ast
import base64
import hashlib
from cryptography.fernet import Fernet
import cryptography
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import InvalidToken
from cryptography.exceptions import InvalidSignature
import binascii







 
 
# output: "aGVsbG8gd29ybGQ"

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
        tempkey = Fernet.generate_key()
        if(os.path.isdir(self.path_(self.database+'/keys/'))==False):
            os.makedirs(self.path_(self.database+'/keys'))
        if(os.path.isfile(self.path_(self.database+f'/keys/{self.bucket_name}.key'))):
            if self._check_key(
                open(
                    
                        self.path_(self.database+f'/keys/{self.bucket_name}.key')
                        ,'rb').read())==True:
                open(self.path_(self.database+f'/keys/{self.bucket_name}.key'),'wb').write(tempkey)
                pass
        else:open(self.path_(self.database+f'/keys/{self.bucket_name}.key'),'wb').write(tempkey)
       
            

        self.key = open(self.path_(self.database+f'/keys/{self.bucket_name}.key'),'rb').read()       
       
        self.fernet = Fernet(self.key)
        if(os.path.exists(self.path_(self.database+'/'+self.bucket_name+'.bdb'))):
 
            _ = open(self.path_(self.database+'/'+self.bucket_name+'.bdb'),'rb').read() 
            
            self.bucket = ast.literal_eval((str(self.fernet.decrypt(_).decode())))
            
        else:
            out__ = open(self.path_(self.database+'/'+self.bucket_name+'.bdb'),'wb')
            out__.write(self.fernet.encrypt(str('[]').encode()))

            
    def _encode_string(self,password: str) -> bytes:
        salt = b'salt_' # Use a unique, random salt for each key
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key






    def _check_key(self,key: bytes) -> bool:
        if len(key) != 32:
            return False
        try:
            base64.urlsafe_b64decode(key)
            return True
        except (TypeError, binascii.Error):
            return False

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
             
                    json_file = open(self.path_(self.database+'/'+self.bucket_name+'.bdb'),'rb').read()
                  
                    data_list = self.fernet.decrypt(json_file).decode()
                
                    # data_list1 = eval(json.dumps(data_list))
                    data_list1 = ast.literal_eval(data_list)
                    data["id"]=str(uuid.uuid1())
           
                    data_list1.append(data)
  
                    outlof = open(self.path_(self.database+'/'+self.bucket_name+'.bdb'),'wb')
                    outfile1 = self.fernet.encrypt(str(data_list1).encode())
                    outlof.write(outfile1)
                
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
        data = ast.literal_eval(query)
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
                    path=self.path_(self.database+'/'+self.bucket_name+'.bdb')
                    json_file = open(self.path_(self.database+'/'+self.bucket_name+'.bdb'),'rb').read()
                    data_list = ast.literal_eval((self.fernet.decrypt(json_file).decode()))
                 
                
                    for data1 in data_list:
                        _ = 0
                        for key,value in query.items():
                            if data1[key]==value:
                                _+=1
                        
                        if _ == len(query.items()):
                            for key1,value1 in data.items():
                            
                                     
                                data1[key1]=value1
                              
                                     
                    outlof = open(self.path_(self.database+'/'+self.bucket_name+'.bdb'),'wb')
                    outfile1 = self.fernet.encrypt(str(data_list).encode())
                    outlof.write(outfile1)
        
        else:raise Exception('No database loaded')
    
   
    def updatebyId(self,id:str,data:dict={}):
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
                    path=self.path_(self.database+'/'+self.bucket_name+'.bdb')
                    json_file = open(self.path_(self.database+'/'+self.bucket_name+'.bdb'),'rb').read()
                    data_list = ast.literal_eval((self.fernet.decrypt(json_file).decode()))
                    
                    for data1 in data_list:
                        if(data1['id']==id):
                            data1.update(data)
                            outlof = open(self.path_(self.database+'/'+self.bucket_name+'.bdb'),'wb')
                            outfile1 = self.fernet.encrypt(str(data_list).encode())
                            outlof.write(outfile1)
                 
                    
        
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
                    json_file = open(self.path_(self.database+'/'+self.bucket_name+'.bdb'),'rb').read()
                    data_list = ast.literal_eval((self.fernet.decrypt(json_file).decode()))
                    path = self.path_(self.database+'/'+self.bucket_name+'.bdb')
                    for data in data_list:
                        _ = 0
                        for key,value in query.items():
                            if data[key]==value:
                                _+=1
                        if _ == len(query.items()):
                            data_list.remove(data)
                    outlof = open(self.path_(self.database+'/'+self.bucket_name+'.bdb'),'wb')
                    outfile1 = self.fernet.encrypt(str(data_list).encode())
                    outlof.write(outfile1)
        
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
                json_file = open(self.path_(self.database+'/'+self.bucket_name+'.bdb'),'rb').read()
                data_list = ast.literal_eval((self.fernet.decrypt(json_file).decode()))
                path = self.path_(self.database+'/'+self.bucket_name+'.bdb')
                with open(path) as json_file:
                    data_list = json.load(json_file)
                    for data in data_list:
                        if(data['id']==id):
                            data_list.remove(data)
                            break
                    outlof = open(self.path_(self.database+'/'+self.bucket_name+'.bdb'),'wb')
                    outfile1 = self.fernet.encrypt(str(data_list).encode())
                    outlof.write(outfile1)
        
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
                path=self.database+'/'+self.bucket_name+'.bdb'
                box  =[]
                json_file = open(self.path_(self.database+'/'+self.bucket_name+'.bdb'),'rb').read()
                data_list = ast.literal_eval((self.fernet.decrypt(json_file).decode()))
                for data in data_list:
                    _ = 0
                    for key,value in query.items():
                       
                            if data[key]==value:
                                _+=1
                    if _ == len(query.items()):
                        box.append(data)
                                
                return box
        
        
        else:raise Exception('No database loaded')
        
        