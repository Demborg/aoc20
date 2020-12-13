from itertools import count
from sys import stdin

t = int(stdin.readline())
bs = [None if b == "x" else int(b) for b in stdin.readline().split(",")]
print(min(((w := b - t % b), b * w) for b in bs if b))

def iter(i=0):
    if i >= len(bs):
        yield from count()
    yield from (t for t in iter(i + 1) if bs[i] is None or (t + i) % bs[i] == 0) 

print(next(iter()))
