import json

x = '{"name": "Farhan", "age": 30, "city": "New York"}'
y = {"name": "Farhan", "age": 30, "city": "New York"}
print(json.loads(x))
print(json.dumps(y, indent=2))

