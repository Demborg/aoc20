from math import prod
from sys import stdin

data = sorted([int(l) for l in stdin.read().split("\n") if l])
diffs = lambda l: (b - a for a, b in zip([0, *l], [*l, data[-1] + 3]))
print(prod(sum(d == i for d in diffs(data)) for i in (1, 3)))

def f(l, floor=0):
    if any(d > 3 for d in diffs(l)):
        return 0
    return 1 + sum(f(l[:i] + l[i + 1:], v) for i, v in enumerate(l) if v > floor) 

print(f(data))
