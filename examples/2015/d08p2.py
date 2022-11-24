from aoc import *
import json

print(sum(map(len, map(json.dumps, lines))) - sum(map(len, lines)))