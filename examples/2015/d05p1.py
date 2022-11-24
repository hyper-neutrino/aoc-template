from aoc import *

t = 0

for x in lines:
    if sum(x.count(a) for a in "aeiou") >= 3 and re.search(r"(.)\1", x) and not re.search("ab|cd|pq|xy", x):
        t += 1

print(t)