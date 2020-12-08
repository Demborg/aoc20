import re
from sys import stdin

program = [[i, int(v)] for i, v in re.findall("(\w{3}) (.\d*)", stdin.read())]

def exec(program, idx, acc, visited):
    if idx >= len(program) or (err := idx in visited):
        return (err, acc) 
    visited.add(idx)
    i, v = program[idx]
    idx += v if i == "jmp" else 1
    acc += v if i == "acc" else 0
    return exec(program, idx, acc, visited)
        
print(exec(program, 0, 0, set())[1])
