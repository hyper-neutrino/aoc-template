from aoc import *

t = 0

for x in lines:
    if re.search(r"(..).*\1", x) and re.search(r"(.).\1", x):
        t += 1

print(t)