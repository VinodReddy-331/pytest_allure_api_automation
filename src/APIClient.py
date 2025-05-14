import requests
from requests import Timeout


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, headers=None, params=None):
        try:
            url = f"{self.base_url}/{endpoint}"
            response = requests.get(url, params=params)
            return response
        except Timeout as errt:
            print(f"Timeout error: {errt}")
        except Exception as error:
            print(error)


    def post(self, endpoint, headers=None, data=None):
        try:
            url = f"{self.base_url}/{endpoint}"
            response = requests.post(url, headers= headers,json=data)
            return response
        except requests.exceptions.Timeout as errt:
            print(f"Timeout error: {errt}")
        except Exception as error:
            print(error)

    def put(self, endpoint, data=None):
        try:
            url = f"{self.base_url}/{endpoint.lstrip('/')}"
            response = requests.put(url, headers=self.headers, json=data)
            return self._handle_response(response)
        except requests.exceptions.Timeout as errt:
            print(f"Timeout error: {errt}")
        except Exception as error:
            print(error)
