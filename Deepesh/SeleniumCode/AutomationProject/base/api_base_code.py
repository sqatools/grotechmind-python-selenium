import requests
import json

class APIBase:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_method(self, object_id, **kwargs):
        if 'headers' in kwargs:
            headers = kwargs['headers']
        else:
            headers = {}
        if 'payload' in kwargs:
            payload = kwargs['payload']
        else:
            payload = {}
        get_url = f"{self.api_url}/{object_id}"
        response = requests.get(get_url, headers=headers, data=payload)
        return response.json(), response.status_code

    def post_method(self, **kwargs):
        if 'headers' in kwargs:
            headers = kwargs['headers']
        else:
            headers = {}
        if 'payload' in kwargs:
            payload = kwargs['payload']
            payload = json.dumps(payload)
        else:
            payload = {}
        get_url = f"{self.api_url}"
        response = requests.post(get_url, headers=headers, data=payload)
        return response.json(), response.status_code