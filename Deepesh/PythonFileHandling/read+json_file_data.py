import json

def read_json_data(filepath):
    with open(filepath, "r") as file:
        data = json.load(file)
        return data


result = read_json_data("read_json_content.json")
print(result)
print(result['Phone'])
