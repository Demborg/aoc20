from sys import stdin

data = [l.split(" ") for l in stdin.read().split("\n") if l]
parsed = [[l[2], l[1][0], [int(i) for i in l[0].split("-")]] for l in data]
print(len([p for p in parsed if p[2][0] <= p[0].count(p[1]) <= p[2][1]]))
print(len([p for p in parsed if sum((p[0][i - 1] == p[1]) for i in p[2]) == 1]))
