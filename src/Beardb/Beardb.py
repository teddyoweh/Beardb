
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
    