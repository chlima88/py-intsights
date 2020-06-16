import os
import requests
import json

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)



class Client:

    def __init__(self, usr=None, pwd=None, domain=None):
        self.usr = usr or os.getenv("INTSIGHTS_USR")
        self.pwd = pwd or os.getenv("INTSIGHTS_PWD")
        self.domain = domain or os.getenv("INTSIGHTS_DOMAIN")
        self.query = ''


    def apiGet(self, resource):

        try:
            response = requests.get(
                f'{self.domain}{resource}',
                auth=(self.usr,self.pwd)
            )
            return response.json()
        except:
            return {"message": "No data"}


    def parseKargs(self, kwargs):

        if kwargs is not None:
            query = '?'
            for key,value in kwargs.items():
                query = f'{query}{key}={value}&'

        return query

    
    def getIocValuesList(self, **kwargs):
        """ Get a simplified version of IOC list from IntSights
        All query params from API are valid arguments. 

        Returns:
            list: A list of dicts with _id, Value as keys.
        """

        query = self.parseKargs(kwargs)
        resource = f'/public/v1/iocs/iocs-values-list{query}'
        print(resource)
        return self.apiGet(resource)



    def getThreatsList(self, **kwargs):

        query = self.parseKargs(kwargs)  
        resource = f'/public/v1/data/threats/threats-list{query}'
        return self.apiGet(resource)


    def getThreatById(self, ThreatIDquery):

        resource = f'/public/v1/data/threats/get-threat/{ThreatIDquery}'
        return self.apiGet(resource)


    def getAssetsTypes(self):

        resource = f'/public/v1/data/assets/assets-types'
        return self.apiGet(resource)


    def getIocByValue(self, **kwargs):
        
        query = self.parseKargs(kwargs)
        resource = f'/public/v1/iocs/ioc-by-value{query}'
        return self.apiGet(resource)





