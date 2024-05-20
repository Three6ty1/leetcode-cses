import sys
from collections import defaultdict
import heapq
from collections import Counter

n = int(input())

res = f"{n}"

while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n *= 3
        n += 1
    res += " " + str(n)

print(res)