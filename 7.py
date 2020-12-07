import re
from itertools import groupby
from sys import stdin

data = [[*i, re.match("\w* \w*", l).group()] for l in stdin.read().split("\n") for i in re.findall("(\d) (\w* \w*)", l)]
back, forward = ({g: list(d) for g, d in groupby(sorted(data, key=k), k)} for k in (lambda x: x[i] for i in (1, 2)))

visited = set()
que = [i[2] for i in back["shiny gold"]]
while que:
    k = que.pop()
    if k not in visited:
        visited.add(k)
        que.extend(i[2] for i in back.get(k, []))
print(len(visited))

counter = 0
que = [(1, "shiny gold")]
while que:
    n, k = que.pop()
    v = forward.get(k, [])
    for i in v:
        counter += n * int(i[0])
        que += [(n * int(i[0]), i[1])]
print(counter)
