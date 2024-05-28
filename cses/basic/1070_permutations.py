n = int(input())

odd = []
even = []

for i in range(1, n + 1):
    if i % 2 == 0:
        even.append(str(i))
    else:
        odd.append(str(i))

if 1 < n < 4:
    print("NO SOLUTION")
else:
    print(" ".join(even) + " " + " ".join(odd))


