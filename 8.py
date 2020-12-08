import re
from sys import stdin

program = [[i, int(v)] for i, v in re.findall("(\w{3}) (.\d*)", stdin.read())]

idx = 0
visited = set()
acc = 0
while idx not in visited:
    visited.add(idx)
    i, v = program[idx]
    if i == "nop":
        idx += 1
    elif i == "acc":
        idx += 1
        acc += v
    elif  i == "jmp":
        idx += v
print(acc)

