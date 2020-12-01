from itertools import combinations
from math import prod
from sys import stdin

data = [int(l) for l in stdin.read().split("\n") if l]
print([next(prod(l) for l in combinations(data, n) if sum(l) == 2020) for n in (2, 3)])
