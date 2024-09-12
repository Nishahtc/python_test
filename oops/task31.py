import requests
import json

response = requests.get("https://api.sampleapis.com/coffee/hot")
data = response.json()

class CoffeeApi:
    def __init__(self, data):
        self.title = data["title"]
        self.image = data["image"]
        self.Cappuccino = data["Cappuccino"]
        
    def get_coffee(self):
        for item in data:
            if item["title"] == "Cappuccino":
                return CoffeeApi(item)

coffee = CoffeeApi(data[0])
print(coffee.Cappuccino)