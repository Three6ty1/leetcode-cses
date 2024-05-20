import sys
from collections import defaultdict
import heapq
from collections import Counter

total = int(input())
nums = set(input().split(" "))

for n in range(1, total + 1):
    if not str(n) in nums:
        print(n)
        break

