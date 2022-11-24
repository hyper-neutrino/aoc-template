from aoc import *

sig = {}

for n in lines:
    l, r = n.split(" -> ")
    try:
        sig[r] = int(l)
    except:
        if l.startswith("NOT"):
            l = l[4:]
            if l in sig:
                sig[r] = 65535 - sig[l]
            else:
                lines.append(n)
                continue
        elif re.match("[a-z]+$", l):
            if l not in sig:
                lines.append(n)
                continue
            sig[r] = sig[l]
        else:
            a, b = re.split(r" [A-Z]+ ", l)
            op = re.search(r"[A-Z]+", l).group()
            try:
                a = int(a)
            except:
                if a not in sig:
                    lines.append(n)
                    continue
                a = sig[a]
            try:
                b = int(b)
            except:
                if b not in sig:
                    lines.append(n)
                    continue
                b = sig[b]
            sig[r] = { "AND": lambda x, y: x & y, "OR": lambda x, y: x | y, "LSHIFT": lambda x, y: (x << y) & 65535, "RSHIFT": lambda x, y: x >> y }[op](a, b)

print(sig["a"])