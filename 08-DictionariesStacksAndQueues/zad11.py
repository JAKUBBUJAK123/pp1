import json

with open("test.json") as file:
    data = json.load(file)

for i in data:
    for k,v in i.items():
        print(f'{k},:,{v}')
