"""
https://discuss.codechef.com/t/coin-piles-problem-from-cses/28647/10
"""
tests = []

for i in range(int(input())):
    left, right = input().split(" ")
    tests.append((int(left), int(right)))

for left, right in tests:   
    if (left + right) % 3 == 0 and 2 * left >= right and 2 * right >= left:
        print("YES")
    else:
        print("NO")
