import json

with open('numbers.json', 'r') as json_file:
    data = json.load(json_file)
    for key in data.keys():
        print(f"data[{repr(key)}] -> {repr(data[key])}")