from itertools import combinations
from sys import stdin
PRE = 25

data = [int(i) for i in stdin.read().split("\n") if i]
inv = next(v for i, v in enumerate(data[PRE:]) if v not in {sum(c) for c in combinations(data[i: PRE + i], 2)})
print(inv)

for i in range(len(data)):
    l = []
    d = 0
    while sum([0, *l]) < inv:
        l.append(data[i+d])
        d += 1    
    if sum(l) == inv and d > 1:
        print(min(l) + max(l))
        

