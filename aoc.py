import re, sys

data = sys.stdin.read()

if data.endswith("\n"):
    data = data[:-1]

original = data
lines = data.split("\n")

py_input = input

def input(overflow = False):
    global data

    if data:
        try:
            line, data = data.split("\n", 1)
        except:
            line = data
            data = ""
        return line

    if not overflow: raise EOFError()
    return py_input()

def getnum(overflow = False):
    global data

    match = re.search(r"\d+(\.\d+)?", data)

    if match:
        num = eval(match.group())
        data = data[match.end():]
        return num
    
    if not overflow: raise EOFError()
    return eval(py_input())

def numrow(overflow = False, incl = False):
    line = input(overflow)
    return ([line] if incl else []) + list([eval(x[0]) for x in re.findall(r"(\d+(\.\d+)?)", line)])

def getchar(allow_whitespace = False):
    global data
    
    if not allow_whitespace:
        data = re.sub(r"^\s+", "", data)
    
    if data:
        char = data[0]
        data = data[1:]
        return char
    
    return py_input()[0]

def rest():
    return data

def is_iter(x):
    return type(x) in [list, tuple, dict, set, map]

def iterize(x):
    return list(x) if is_iter(x) else [x]

def depth(x):
    return 0 if not is_iter(x) else min(map(depth, x)) + 1

def depth_max(x):
    return 0 if not is_iter(x) else max(map(depth, x)) + 1

def force_depth(x, d):
    return x if depth(x) >= d else [force_depth(y, d - 1) for y in iterize(x)]

py_zip = zip

def zip(*a, mode = "loop"):
    a = [iterize(x) or [0] for x in a]
    b = []

    for i in range(max(map(len, a))):
        if mode == "loop":
            b.append([x[i % len(x)] for x in a])
        elif mode == "pad":
            b.append([x[i] if i < len(x) else 0 for x in a])
        elif mode == "truncate":
            if any(i >= len(x) for x in a):
                return b
            b.append([x[i] for x in a])

    return b

def ft(x):
    print(x)
    return x

def vectorize(*indexes, depths = [0], mode = "pad"):
    def inner(fn):
        def _fn(*args):
            args = list(args)
            il = indexes or list(range(len(args)))
            if all(depth(args[x]) <= d for x, d in zip(il, depths)):
                for x, d in zip(il, depths):
                    args[x] = force_depth(args[x], d)
                return fn(*args)
            o = []
            for k in zip(*(args[x] for x in il), mode = mode):
                for a, x in py_zip(k, il):
                    args[x] = a
                o.append(_fn(*args))
            return o
        return _fn
    return inner

def filter(predicate, array):
    return [x for x in iterize(array) if predicate(x)]

@vectorize()
def add(*x):
    return sum(x)

@vectorize()
def mul(*x):
    return reduce(x, lambda x, y: x * y)

@vectorize()
def sub(*x):
    return reduce(x, lambda x, y: x - y)

@vectorize()
def div(*x):
    return reduce(x, lambda x, y: x / y)

@vectorize()
def exp(*x):
    return rreduce(x, lambda x, y: x ** y)

def translate(a, *x):
    if len(x) % 2 != 0: raise RuntimeError("odd # of arguments to translate")

    for i in range(len(x) // 2):
        v = iterize(x[i * 2])
        w = iterize(x[i * 2 + 1])
        for i, o in zip(v, w):
            a = [o if k == i else k for k in a]
    
    return a

def reduce(a, f, s = None):
    a = iterize(a) or [0]
    if s is not None: a.insert(0, s)
    while len(a) > 1:
        a[:2] = [f(a[0], a[1])]
    return a[0]

def rreduce(a, f, s = None):
    a = iterize(a) or [0]
    if s is not None: a.append(s)
    while len(a) > 1:
        a[-2:] = [f(a[-2], a[-1])]
    return a[0]

def creduce(a, f, s = None):
    a = iterize(a)
    if len(a) == 0: return a
    o = [s if s is not None else a.pop(0)]
    for x in a:
        o.append(f(o[-1], x))
    return o

def crreduce(a, f, s = None):
    a = iterize(a)
    if len(a) == 0: return a
    o = [s if s is not None else a.pop()]
    for x in a[::-1]:
        o.append(f(x, o[-1]))
    return o

def sliding(a, n, f = lambda *a: [*a], loop = True):
    o = []

    cap = len(a) if loop else len(a) - n + 1
    if loop: a = a + a[:n - 1]

    for i in range(cap):
        o.append(f(*a[i:i + n]))
    
    return o

def pairs(a, f = lambda x, y: [x, y], loop = True):
    return sliding(a, 2, f, loop)

def nfurcate(a, n):
    o = [[] for _ in range(n)]
    for i in range(len(a)):
        o[i % n].append(a[i])
    return o

def bifurcate(a):
    return nfurcate(a, 2)

def flat(x):
    if depth(x) <= 1:
        return iterize(x)
    return sum([flat(a) for a in x], [])