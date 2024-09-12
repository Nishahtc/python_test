import requests
import json
respons=requests.get("https://api.sampleapis.com/coffee/hot")
respons=respons.json()
class CoffeeApi():
    def __init__(self,data):
        self.title=data["title"]
        self.image=data["image"]
        self.Cappuccino=data["Cappuccino"]
    def getcoffee(self):
        for i in respons:
            if i ["title"]=="Cappuccino":
                data=CoffeeApi(i)
                return data
responslessclass=CoffeeApi()   
print(responslessclass.Cappuccino)
            


