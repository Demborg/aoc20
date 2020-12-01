data = [int(l) for l in open("1.txt").read().split("\n") if l]

print([(a * b) for a in data for b in data if a + b == 2020])
