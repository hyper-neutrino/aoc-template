from aoc import *
import json

data = json.loads(data)

def s(x):
    if type(x) == int:
        return x
    elif type(x) == list:
        return sum(map(s, x))
    elif type(x) == dict:
        if "red" in x.values():
            return 0
        return sum(map(s, x.values()))
    return 0

print(s(data))