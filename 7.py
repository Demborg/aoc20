import re
from itertools import groupby
from sys import stdin

data = [[i, re.match("\w* \w*", l).group()] for l in stdin.read().split("\n") for i in re.findall("\d (\w* \w*)", l)]
grouped = {g: list(d) for g, d in groupby(sorted(data, key=lambda x: x[0]), lambda x: x[0])}

visited = set()
que = [i[1] for i in grouped["shiny gold"]]
while que:
    v = que.pop()
    if v not in visited:
        visited.add(v)
        que.extend(i[1] for i in grouped.get(v, []))
print(len(visited))
