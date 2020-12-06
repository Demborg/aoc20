from functools import reduce
from sys import stdin

data = [[{q for q in p} for p in g.split("\n") if p] for g in stdin.read().split("\n\n")]
print([sum(len(reduce(f, g)) for g in data) for f in (set.union, set.intersection)])
