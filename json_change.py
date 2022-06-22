import json
import os
from pathlib import Path

def json_make(path: Path, obj: dict) -> None:
    ls = None
    with open(path, 'r+') as f:
        ls = f.readlines()
        if ls == []:
            ls.append('[\n')
        if ls[-1] == ']':
            ls[-1] = ','
        ls.insert(len(ls), f'{json.dumps(obj, indent=4 ,ensure_ascii=False)}')
        ls.insert(len(ls), '\n]')

    with open(path, 'w') as f:
        f.writelines(ls)

raw = open("pref_city.json","r")
parsed = json.load(raw)
path = Path(__file__).parent/'city_code.json'

target = {}
for t in parsed[0]:
    dict_obj = {}
    for cityname in parsed[0][t]["city"]:
        dict_obj[cityname["city"]] = cityname["citycode"]
    target[parsed[0][t]["name"]] = dict_obj

print(type(target))
json_make(path,target)