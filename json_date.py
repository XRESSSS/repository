import json

data = {
    'key': 'My surname',
    'another_key': [55, 66],
    'one_more_key': None,
}

json_string = json.dumps(data)
print(json_string)

data_from_json = json.loads(json_string)
print(data_from_json)

with open('data.json', mode='w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)

with open('data.json') as file:
    data_ = json.load(file)
    print(data_)
