from aoc import *
from itertools import groupby

for _ in range(50):
    data = "".join(str(len(list(l))) + v for v, l in groupby(data))

print(len(data))