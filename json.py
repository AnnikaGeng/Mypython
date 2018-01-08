import json

obj = dict(name='ming', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)