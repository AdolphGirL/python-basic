# -*- coding: utf-8 -*-

import json

# json dict to str
data = {'today': 9, 'is': '123'}
output = json.dumps(data)
print(output)

# json str to dict
data = '''
{"a": 100, "b": "1000"}
'''
load_data = json.loads(data)
print(load_data)

# dict to json file
data = {'a': 100, 'b': 1000, 'c': 10000}
with open('abc.json', 'w', encoding='utf-8') as f:
    json.dump(data, f)

# json file to dict
load_data = None
with open('abc.json', 'r', encoding='utf-8') as f:
    load_data = json.load(f)
print(load_data)

# load json file to json array and print
# 另一種寫法
load_data = open('efg.json', 'r', encoding='utf-8')
load_data = json.load(load_data)
print(type(load_data))