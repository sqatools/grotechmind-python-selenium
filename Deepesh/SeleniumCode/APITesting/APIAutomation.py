"""
HTTP Method:

GET
POST
PUT
UPDATE
DELETE
PATCH

100-
200- Success
300- Redirection
400- Client Side Error
500- Server side Error

https://www.goibibo.com/flights/

protocol : https
server address : www.goibibo.com
Api end point : /flights/
"""

import requests

# get object details
def get_list_object():
    response = requests.get("https://api.restful-api.dev/objects")

    print(response.status_code)
    data = response.json()
    for info in data:
        print(info)

print("_"*50)
# get specific object details

def get_specific_objects():
    response = requests.get("https://api.restful-api.dev/objects?id=3&id=5&id=10")

    print(response.json())


def postman_code():
    import requests

    url = "https://api.restful-api.dev/objects?id=3&id=5&id=10"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)


postman_code()










