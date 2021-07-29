import json


result = json.dumps({'jack' : 4098, 'sape' : 4139})

print(type(result))
print(result)

result = json.loads(result)

print(type(result))
print(result)