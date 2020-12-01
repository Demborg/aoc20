from itertools import combinations
from math import prod
from sys import stdin
data = [int(l) for l in stdin.read().split("\n") if l]

print(next(prod(l) for l in combinations(data, 2) if sum(l) == 2020))
print(next(prod(l) for l in combinations(data, 3) if sum(l) == 2020))
