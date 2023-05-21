import json

with open('data/credit-g.json', 'r') as f:
    data = json.load(f)

print(f"number of keys: {len(data)}")
print(f"type of keys: {type(data)}")
print(f"sample dict:\n {json.dumps(data[10], indent=4)}")
