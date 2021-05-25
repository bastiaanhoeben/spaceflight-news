import requests
import json


class Retrieval:

    def __init__(self, url):
        self.url = url

    def retrieve_json(self, limit):
        full_url = f"{self.url}?_limit={limit}"
        fhand = requests.get(full_url)
        data = fhand.text
        js = json.loads(data)
        print(f"{len(js)} articles retrieved")
        return js