from itertools import count
from sys import stdin

t = int(stdin.readline())
bs = [None if b == "x" else int(b) for b in stdin.readline().split(",")]
print(min(((w := b - t % b), b * w) for b in bs if b))
max_b, max_i = max((b, i) for i, b in enumerate(bs) if b)
print(next(t for t in count(max_b - max_i, max_b) if all((t + i) % b == 0 for i, b in enumerate(bs) if b)))
