from sys import stdin

ids = [sum( 2 ** i * (c in "BR") for i, c in enumerate(l[9::-1])) for l in stdin.readlines()]
print(max(ids))
print(next(v for v in range(min(ids), max(ids)) if v not in ids))
