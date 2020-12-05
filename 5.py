from sys import stdin

def decode(data, c):
    return sum(2 ** i * (d == c) for i, d in enumerate(data))

data = [[decode(l[6::-1], "B"), decode(l[9:6:-1], "R")] for l in stdin.readlines()]
ids = [d[0] * 8 + d[1] for d in data]

print(max(ids))
print([v for v in range(min(ids), max(ids)) if v not in ids])
