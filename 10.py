from sys import stdin

data = [int(l) for l in stdin.read().split("\n") if l]
data = [0, *sorted(data), 3+max(data)]
diffs = [b - a for a, b in zip(data, data[1:])]
print(sum(d == 1 for d in diffs) * sum(d == 3 for d in diffs))
