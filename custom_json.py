import json

def read_json_file(file_path):
    with open(file_path, "r") as file:
        content = json.load(file)
    return content

file_path = "example.json"
content = read_json_file(file_path)
print(content)
