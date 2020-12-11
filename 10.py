from math import prod
from sys import stdin
from itertools import groupby

data = sorted([int(l) for l in stdin.read().split("\n") if l])
data = [0, *data, max(data) + 3]
print(prod(sum(b - a == i for a, b in zip(data, data[1:])) for i in (1, 3)))

tree = {l: [x[1] for x in g] for l, g in groupby([(i, j) for i in data for j in data if j > i and j - i < 4], lambda x: x[0])}

mem = {}
def f(v):
    if v not in mem:
        mem[v] = 1 if v == max(data) else sum(f(n) for n in tree[v])
    return mem[v]
    

print(f(0))
