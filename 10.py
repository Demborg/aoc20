from math import prod
from sys import stdin

data = sorted([int(l) for l in stdin.read().split("\n") if l])
diffs = lambda l: (b - a for a, b in zip([0, *l], [*l, data[-1] + 3]))
print(prod(sum(d == i for d in diffs(data)) for i in (1, 3)))
