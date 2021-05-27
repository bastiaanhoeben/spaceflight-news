import requests
import json


class Retrieval:
    """Class for interacting with the Spaceflight News API"""
    def __init__(self, url):
        self.url = url

    def retrieve_json(self, limit):
        """Takes a article retrieval limit, returns a json file with retrieved data"""
        full_url = f"{self.url}?_limit={limit}"
        fhand = requests.get(full_url)
        data = fhand.text
        js = json.loads(data)
        print(f"\n{len(js)} articles retrieved")
        return js