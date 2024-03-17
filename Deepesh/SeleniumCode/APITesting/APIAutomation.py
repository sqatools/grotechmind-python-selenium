import requests
from requests.auth import HTTPBasicAuth

username = 'TusharAher3131'
password = 'Poiuy@5412'
response = requests.get("https://api.github.com/user", auth=HTTPBasicAuth(username, password), verify=False)
print(response.text)
print(response.json())
print(response.status_code)