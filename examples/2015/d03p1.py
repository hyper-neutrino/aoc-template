from aoc import *

print(len(set(creduce(translate(q, ">", 1, "<", -1, "^", 1j, "v", -1j), add, 0) for q in bifurcate(data))))