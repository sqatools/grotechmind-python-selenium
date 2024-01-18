import json

def Read_json_data(filepath):
    with open(filepath, "r") as file:
        data = json.load(file)
        return data

Result = Read_json_data("Read_json_content.json")
print(Result)
print()
