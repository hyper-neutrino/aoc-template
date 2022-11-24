from aoc import *

x = [ord(c) - 97 for c in data]

b = 0

while True:
    x[-1] += 1
    if x[-1] >= 26:
        i = -1
        while x[i] >= 26:
            x[i] = 0
            x[i - 1] += 1
            i -= 1
    y = "".join(chr(k + 97) for k in x)
    if not re.search(r"[iol]", y) and re.search(r"(.)\1.*(.)\2", y) and any(sliding(x, 3, lambda a, b, c: a + 1 == b == c - 1, False)):
        b += 1
        if b == 2: break

print(y)