import requests
import json

response=requests.get("https://api.sampleapis.com/coffee/hot")
response=response.json()
class Coffee(object):
    def _init_(self,data):
        self._dict_=data
    
        
def display():
    
    for v in response :
        if v ['title']=='Cappucciano':
            data=Coffee(v)
            return data
            
responseinclass=display()
print(responseinclass.title)

print(json.dumps(responseinclass._dict_,indent=4))