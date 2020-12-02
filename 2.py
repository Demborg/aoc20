from sys import stdin

data = [l.split(" ") for l in stdin.read().split("\n") if l]
parsed = [[l[2].count(l[1][0]), [int(i) for i in l[0].split("-")]] for l in data]
print(len([p for p in parsed if p[1][0] <= p[0] <= p[1][1]]))
