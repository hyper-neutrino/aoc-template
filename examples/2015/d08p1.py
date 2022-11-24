from aoc import *

print(sum(map(len, lines)) - sum(map(len, map(eval, lines))))