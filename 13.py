from itertools import count
from sys import stdin
from math import prod

t = int(stdin.readline())
bs = [(int(b), i) for i, b in enumerate(stdin.readline().split(",")) if b != "x"]
print(min(((w := b - t % b), b * w) for b, _ in bs))

print(
        sum(
            next(
                n for j in range(b1) 
                if (n := (j * prod(
                    b2 for b2, _ in bs if b2 != b1
                ))) % b1 == -i % b1
            )
            for b1, i in bs
        ) 
        % prod(b for b, i in bs)
)
