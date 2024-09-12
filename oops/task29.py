import requests
import json
respons=requests.get("https://api.sampleapis.com/coffee/hot")
respons=respons.json()
class CoffeeApi(object):
    def __init__(self,data):
        self.__dict__=data
    def getcoffee(self):
        for i in respons:
            if i ["title"]=="Cappuccino":
                data=CoffeeApi(i)
                return data
responslee=getcoffee()








