from itertools import count
from sys import stdin

t = int(stdin.readline())
bs = sorted([(int(b), i) for i, b in enumerate(stdin.readline().split(",")) if b != "x"])
print(min(((w := b - t % b), b * w) for b, _ in bs))

def iter(i=0):
    b, j = bs[i]
    if i == len(bs) - 1:
        yield from count(b - j, b)
    yield from (t for t in iter(i + 1) if (t + j) % b == 0) 

print(next(iter()))
