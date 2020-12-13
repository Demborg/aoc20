from math import ceil
from sys import stdin

t = int(stdin.readline())
bs = [int(b) for b in stdin.readline().split(",") if b != "x"]
print(t, bs)

print(min(((w := b * ceil(t / b) - t), b * w) for b in bs))
