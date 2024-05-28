n = int(input())
apples = sorted([int(x) for x in input().split(" ")])[::-1]

# greedy matching?

s1 = 0
s2 = 0

for a in apples:
    if s1 > s2:
        s2 += a
    else:
        s1 += a


print(abs(s1 - s2))