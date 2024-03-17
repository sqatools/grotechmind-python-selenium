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
import json

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


# postman_code()

def get_single_object(object_id):
    payload = {}
    headers = {}
    response = requests.get(f"https://api.restful-api.dev/objects/{object_id}", headers=headers, data=payload)
    print(response.json())
    # {'id': '8', 'name': 'Apple Watch Series 8', 'data': {'Strap Colour': 'Elderberry', 'Case Size': '41mm'}}

#get_single_object(8)

def add_object_with_post_method():
    payload = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 1849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
            }
        }
    json_data = json.dumps(payload)

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post("https://api.restful-api.dev/objects", headers=headers, data=json_data)
    print(response.json())
    print(response.status_code)

#add_object_with_post_method()
# {'error': '415 Unsupported Media Type. The 415 status code indicates
# that the origin server is refusing to service the request because the
# payload is in a format not supported by this method on the target
# resource. One of the examples of getting 415 would be sending a request
# with a Content-Type header which is not equal to application/json'}


def update_details_with_put_method(object_id):
    payload_data = json.dumps(
        {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 10000,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB",
                "color": "silver"
            }
        }
    )

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.put(f"https://api.restful-api.dev/objects/{object_id}", headers=headers, data=payload_data)
    print(response.json())
    print(response.status_code)




#update_details_with_put_method("ff8081818dfdd992018e16df818c1c88")
"""
{'id': 'ff8081818dfdd992018e16df818c1c88', 'name': 'Apple MacBook Pro 16',
 'updatedAt': '2024-03-07T03:06:50.791+00:00', 
 'data': {'year': 2019, 'price': 10000, 'CPU model': 'Intel Core i9', 
 'Hard disk size': '1 TB', 'color': 'silver'}}
"""
#get_single_object("ff8081818dfdd992018e16df818c1c88")

# patch method
def update_partial_details(object_id):
    payload_data = json.dumps(
        {
            "name": "Apple MacBook Pro 17 (update name)",
        }
    )

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.patch(f"https://api.restful-api.dev/objects/{object_id}", headers=headers, data=payload_data)
    print(response.json())
    print(response.status_code)


#update_partial_details("ff8081818dfdd992018e16df818c1c88")


def delete_method(object_id):
    payload_data = {}
    headers = {}

    response = requests.delete(f"https://api.restful-api.dev/objects/{object_id}", headers=headers, data=payload_data)
    print(response.json())
    print(response.status_code)


delete_method("ff8081818dfdd992018e16df818c1c88")
# {'message': 'Object with id = ff8081818dfdd992018e16df818c1c88 has been deleted.'}
