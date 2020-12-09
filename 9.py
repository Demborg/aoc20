from itertools import combinations
from sys import stdin
PRE = 25

data = [int(i) for i in stdin.read().split("\n") if i]
print(next(v for i, v in enumerate(data[PRE:]) if v not in {sum(c) for c in combinations(data[i: PRE + i], 2)}))
