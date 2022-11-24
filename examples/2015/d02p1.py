from aoc import *

t = 0

while True:
    try:
        x = numrow()
        a = pairs(x, mul)
        t += 2 * sum(a) + min(a)
    except:
        break

print(t)