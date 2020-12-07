import re
from itertools import groupby
from sys import stdin

data = [[re.match("\w* \w*", l).group(), i, n] for l in stdin.read().split("\n") for n, i in re.findall("(\d) (\w* \w*)", l)]
print(data)
grouped = {g: l for g, d in groupby(data, lambda x: x[1]) if len(l := list(d))}
print(grouped)

visited = set()
que = [i[0] for i in grouped.get("shiny gold", [])]
while que:
    v = que.pop()
    if v not in visited:
        visited.add(v)
        que.extend(i[0] for i in grouped.get(v, []))
print(visited)
