import json
class Client:
 
    def __init__(self, config):
        self.config = config
        self.configdata = {}
    def config(self,email,secret):
        self.configdata = {}
        self.configdata['email'] = email
        self.configdata['secret'] = secret
    