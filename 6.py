from sys import stdin

data = [[{q for q in p} for p in g.split("\n") if p] for g in stdin.read().split("\n\n")]
print(sum(len({q for p in g for q in p}) for g in data))
