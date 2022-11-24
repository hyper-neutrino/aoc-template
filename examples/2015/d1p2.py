from aoc import *

print(creduce(translate(data, "(", 1, ")", -1), add).index(-1) + 1)