import requests
import json
class API:
    def __init__(self, base_url):
        self.base_url = base_url
        
    def get_data(self, endpoint):
        url = self.base_url + endpoint
        response = requests.get(url)
        return response.json()
api = API("https://api.sampleapis.com/coffee/hot")
print(api.get_data("/users"))
