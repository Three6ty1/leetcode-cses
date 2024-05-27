"""
https://www.youtube.com/watch?v=OtZ81ydc3WA
"""

n = int(input())

sum = 0
nums = []

for i in range(1, n + 1):
    sum += i
    nums.append(str(i))

if sum % 2 == 1:
    print("NO")

else:
    s1 = []
    s2 = []
    if n % 2 == 0:
        lo = 0
        hi = n - 1
        while lo < hi:
            if lo % 2 == 0:
                s1.append(nums[lo])
                s1.append(nums[hi])
            else:
                s2.append(nums[lo])
                s2.append(nums[hi])
            lo += 1
            hi -= 1

    else:
        lo = 0
        hi = n - 2

        while lo < hi:
            if lo % 2 == 0:
                s1.append(nums[lo])
                s1.append(nums[hi])
            else:
                s2.append(nums[lo])
                s2.append(nums[hi])
            lo += 1
            hi -= 1

        s2.append(str(n))

    print("YES")
    print(len(s1))
    print(" ".join(s1))
    print(len(s2))
    print(" ".join(s2))
            