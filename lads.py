import json 
data = json.loads('{"name": "Gad"}')
text = json.dumps(data, indent=2)
print(text)
with open("data.json") as f:
    data = json.load(f)
    print(data)