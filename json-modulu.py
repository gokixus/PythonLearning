import json

person_string = '{"name":"Ali", "languages":["Python", "C#"]}'

result1 = json.loads(person_string)
print(result1)

with open("person.json") as file:
    data = json.load(file)
    print(data)
    print(data["name"])
    print(data["languages"])
    
person_dict = {
    "name": "Ali",
    "languages": ["Python", "Javascript"]
}

result2 = json.dumps(person_dict)
print(result2)


with open("person.json", "w") as f:
    json.dump(person_dict, f)
