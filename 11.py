from sys import stdin

data = [[c for c in l] for l in stdin.read().split("\n") if l]

def check_occupied(state, i, j):
    if 0 <= i < len(state) and 0 <= j < len(state[i]):
        return state[i][j] == "#"
    return False

def new(state, i, j):
    n = sum(check_occupied(state, i + v, j + u) for u in (-1, 0, 1) for v in (-1, 0, 1) if u != 0 or v != 0)
    if state[i][j] == "L":
        return "#" if n == 0 else "L"
    if state[i][j] == "#":
        return "L" if n >= 4 else "#"
    return state[i][j]

def update(state):
    return [[new(state, i, j) for j in range(len(state[i]))] for i in range(len(state))] 

while data != (data := update(data)):
    pass

print(sum(check_occupied(data, i, j) for i in range(len(data)) for j in range(len(data[i]))))
