import sys
data = [int(l) for l in sys.stdin.read().split("\n") if l]

print([(a * b) for a in data for b in data if a + b == 2020])
print([(a * b * c) for a in data for b in data for c in data if sum((a, b, c)) == 2020])
