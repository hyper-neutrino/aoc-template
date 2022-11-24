from aoc import *

g = {}
l = set()

for n in lines:
    a, b, d = re.match(r"(\w+) to (\w+) = (\d+)", n).groups()
    d = int(d)
    l.add(a)
    l.add(b)
    if a not in g: g[a] = {}
    g[a][b] = d
    if b not in g: g[b] = {}
    g[b][a] = d

import itertools

print(max(sum(pairs(x, lambda a, b: g.get(a, {}).get(b, float("inf")), False)) for x in itertools.permutations(l)))