import json
import pandas as pd
with open('data/credit-g.json', 'r') as f:
    data = json.load(f)

print(f"number of keys: {len(data)}")
print(f"type of keys: {type(data)}")
print(f"sample dict:\n {json.dumps(data[10], indent=4)}")

df = pd.DataFrame.from_records(data)
df.to_csv('data/credit.csv', index=False)
