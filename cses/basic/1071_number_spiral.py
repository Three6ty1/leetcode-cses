n = int(input())

for _ in range(n):
    x, y = [int(x) for x in input().split(" ")]
    
    bigger = max(x, y)
    smaller = min(x, y)
    top = bigger * bigger
    bot = top - (bigger + bigger - 2)
    
    if bigger % 2 == 0:
        if x > y:
            print(top - (y - 1))
        else:
            print(bot + (x - 1))
    else:
        if x > y:
            print(bot + (y - 1))
        else:
            print(top - (x - 1))

