from aoc import *

g = [[0] * 1000 for _ in range(1000)]

while True:
    try:
        m, x1, y1, x2, y2 = numrow(incl = True)
        f = (lambda _: 1) if m.startswith("turn on") else (lambda _: 0) if m.startswith("turn off") else (lambda x: 1 - x)
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                g[x][y] = f(g[x][y])
    except:
        break

print(sum(map(sum, g)))