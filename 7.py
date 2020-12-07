import re
from itertools import groupby
from sys import stdin

data = [[*i, re.match("\w* \w*", l).group()] for l in stdin.read().split("\n") for i in re.findall("(\d) (\w* \w*)", l)]
b, f = ({g: list(d) for g, d in groupby(sorted(data, key=k), k)} for k in (lambda x: x[i] for i in (1, 2)))

def one(key):
    return set.union({key}, *(one(i[2]) for i in b.get(key, [])))
print(len(one("shiny gold")) - 1)

def two(key, n=1):
    return n + sum(two(i[1], n * int(i[0])) for i in f.get(key, []))
print(two("shiny gold") - 1)

