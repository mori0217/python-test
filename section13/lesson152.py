import json

j = {
    "employees": [
        {
            "id": "111",
            "name": "Mike"
        },
        {
            "id": "222",
            "name": "Nancy"
        },
    ]
}

print(type(j))
print(j)
json_str = json.dumps(j)
print(type(json_str))
print(json_str)
print(type(json.loads(json_str)))
print(json.loads(json_str))

with open('section13/test.json', 'w') as f:
    json.dump(j, f)

with open('section13/test.json', 'r') as f:
    json_dict = json.load(f)
    print(type(json_dict))
    print(json_dict)
