from sys import stdin

data = [{q for p in g.split("\n") for q in p} for g in stdin.read().split("\n\n")]
print(sum(len(g) for g in data))
