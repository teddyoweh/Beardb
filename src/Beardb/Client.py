import json
import ssl
import socket
import functools
import threading
import time
import requests
class Client:
 
    def __init__(self,host:str,port:int,email:str,secret:str ):
        """
        Client Object which fetches data from the API.
    
        """
        
 
        self.configdata = {}
        self._config(host,port,email,secret)
        self._headers = {'Content-Type': 'application/json'}
        self.host =''
        self.port =''
    def _ishttps(self,host:str, port:int):
        """
        Checks if the host is using https.
        """
        ""
        context = ssl.create_default_context()
        try:
            with context.wrap_socket(socket.socket(), server_hostname=host) as s:
                s.connect((host, port))
                return True
        except ssl.SSLError:
            return False
    @staticmethod
    def _config(self,host:str,port:int,email:str,secret:str):
        """
        Configures the API client.
        args:
            host:
            port:str (optional)
            email:str
            secret:str

        """
    
        self.configdata = {}
        self.host = host
        self.port = port
        self.configdata['email'] = email
        self.configdata['secret'] = secret
        self.routes
    @staticmethod
    def _merge(self,*args):
        """
        Merges multiple params with api auth.
        """
        merged = self.routes
        for dictionary in args:
            for key, value in dictionary.items():
                merged[key] = value
        return merged
        
    @property
    def address(self):
        
        return self.host + ':' + str(self.port)

    @property
    def headers(self):
        return self.headers
    @staticmethod
    def grab(self,data:dict,url):
        """
        Grabs the data from the API.
        args:
            data:dict
            url:str
       
        returns:

            {
                'status':str,
                'data':dict,
            }
   
        """
    
        response = requests.post(self.routes[url], data=data, headers=self.headers)
        return {'status':response.status_code,
                'data':response.json()}
        


    @property
    @functools.lru_cache
    def routes(self):
        """
            Returns a dictionary of routes.
        """
        routes = {
            'me':f'{self.address}/me',
            'newuser':f'{self.address}/newuser',
            'newproject':f'{self.address}/newproject',
            'newdatabase':f'{self.address}/newdatabase',
            'newbucket':f'{self.address}/newbucket',
            'insertdata':f'{self.address}/insertdata',
            'fetchdata':f'{self.address}/fetchdata',
            'fetchbyid':f'{self.address}/fetchbyid',
            'updatedata':f'{self.address}/updatedata',
            'updatebyid':f'{self.address}/updatebyid',
            'deletedata':f'{self.address}/deletedata',
            'deletebyid':f'{self.address}/deletebyid',
            'getbuckets':f'{self.address}/getbuckets',
            'getdatabases':f'{self.address}/getdatabases',
            'getprojects':f'{self.address}/getprojects',
        }
        
        return routes
    
    def createnewuser(self,fullname:str,email:str, password:str):
        """
        Creates a new user.
        ```
        args:
            email:str
            password:str
            fullname:str
        ```
        """
        body = self._merge({'email':email,'password':password,'fullname':fullname})
        return self.grab(body=body,url='newuser')


    
    
        pass
    def createnewproject(self,project:str):
        """
        Creates a new project.
        ```
        args:
            project:str
        ```
        """
        body = self._merge({'project':project})
        return self.grab(body=body,url='newproject')
    
    def createnewdatabase(self,database:str,project:str):
        """
        Creates a new database.
        ```
        args:
            database:str
            project:str

        returns:
        ```
        {
           'status':str,
            'data':dict,
        }
        ```
        """
        body = self._merge({'database':database,'project':project})
        return self.grab(body=body,url='newdatabase')
    
    def createnewbucket(self,bucket:str,database:str,project:str):
        """
        Creates a new bucket.
        ```
        args:
            bucket:str
            database:str
            project:str
        """
        body = self._merge({'bucket':bucket,'database':database,'project':project})
        return self.grab(body=body,url='newbucket')
    
    def insertdata(self,data:dict,bucket:str,database:str,project:str):
        """
        Creates a new data.
        ```
        args:
            data:dict
            bucket:str
            database:str
            project:str
        ```
        """
        body = self._merge({'data':data,'bucket':bucket,'database':database,'project':project})
        return self.grab(body=body,url='insertdata')

    def updatedata(self,query:dict,data:dict,bucket:str,database:str,project:str):
        """
        Updates a data.
        ```
        args:
            query:dict
            data:dict
            bucket:str
            database:str
            project:str
        ```
        """
        body = self._merge({'query':query,'data':data,'bucket':bucket,'database':database,'project':project})
        return self.grab(body=body,url='updatedata')
    def updatebyid(self,id:str,data:dict,bucket:str,database:str,project:str):
        """
        Updates a data.
        ```
        args:
            id:str
            data:dict
            bucket:str
            database:str
            project:str
        ```
        """
        body = self._merge({'id':id,'data':data,'bucket':bucket,'database':database,'project':project})
        return self.grab(body=body,url='updatebyid')
    
    def fetchdata(self,query:dict,bucket:str,database:str,project:str):
        """
        Fetches data in bucket.
        ```
        args:
            query:dict
            bucket:str
            database:str
            project:str
        ```
        """
        body = self._merge({'query':query,'bucket':bucket,'database':database,'project':project})
        return self.grab(body=body,url='fetchdata')
    def fetchdatabyid(self,id:str,bucket:str,database:str,project:str):
        """
        Fetches data in bucket by id.
        ```
        args:
            id:str
            bucket:str
            database:str
            project:str
        ```
        """
        body = self._merge({'id':id,'bucket':bucket,'database':database,'project':project})
        return self.grab(body=body,url='fetchdatabyid')
    def deletedata(self,data:dict,bucket:str,database:str,project:str):
        """
        Deletes a data.
        ```
        args:
            data:dict
            bucket:str
            database:str
            project:str
        ```
        """
        
        body = self._merge({'data':data,'bucket':bucket,'database':database,'project':project})
        return self.grab(body=body,url='deletedata')
    def deletebyid(self,id:str,bucket:str,database:str,project:str):
        """
        Deletes a data in a bucket by id.
        ```
        args:
            id:str
            bucket:str
            database:str
            project:str
        ```
        """
        body = self._merge({'id':id,'bucket':bucket,'database':database,'project':project})
        return self.grab(body=body,url='deletebyid')
    
    def getbuckets(self):
        """
        Gets all buckets.
        ```
       
        ```

        """
        body = self._merge({})
        return self.grab(body=body,url='getbuckets')
    def getdatabases(self):
        """
        Gets all databases.
        ```
       
        """
        body = self._merge({})
        return self.grab(body=body,url='getdatabases')
    def getprojects(self):
        """
        Gets all projects.
        ```

        """
        body = self._merge({})
        return self.grab(body=body,url='getprojects')

    


