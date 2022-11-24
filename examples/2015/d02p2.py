from aoc import *

t = 0

while True:
    try:
        x = numrow()
        t += 2 * min(pairs(x, add)) + mul(*x)
    except:
        break

print(t)