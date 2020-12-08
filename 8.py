import re
from sys import stdin

program = [[i, int(v)] for i, v in re.findall("(\w{3}) (.\d*)", stdin.read())]

def exec(program, visited, idx=0, acc=0):
    if (end := idx >= len(program)) or idx in visited:
        return (end, acc) 
    visited.add(idx)
    i, v = program[idx]
    idx += v if i == "jmp" else 1
    acc += v if i == "acc" else 0
    return exec(program, visited, idx, acc)
        
print(exec(program, set())[1])
print(next(r for r in (exec([*program[:idx], ["jmp" if i == "nop" else "nop", v], *program[idx + 1:]], set()) for idx, (i, v) in enumerate(program) if i != "acc") if r[0]))
