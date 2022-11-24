from aoc import *
import hashlib

i = 0

while not hashlib.md5(bytes(data + str(i), "utf8")).hexdigest().startswith("0" * 5):
    i += 1

print(i)