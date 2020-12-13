from sys import stdin

t = int(stdin.readline())
bs = [None if b == "x" else int(b) for b in stdin.readline().split(",")]
print(min(((w := b - t % b), b * w) for b in bs if b))
