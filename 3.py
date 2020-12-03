from sys import stdin
from math import prod

data = [[c == "#" for c in r.strip("\n")] for r in stdin.readlines() if r]
print(sum(r[(i * 3) % len(r)] for i, r in enumerate(data)))
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
print(prod(sum(data[i][int(s[0] / s[1] * i) % len(data[0])] for i in range(0, len(data), s[1])) for s in slopes))

