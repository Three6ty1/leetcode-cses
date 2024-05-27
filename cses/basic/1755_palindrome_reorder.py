from collections import Counter

string = str(input())

hashmap = Counter(string)

odd = ""
res = ""
for letter, amt in hashmap.items():
    if amt % 2 == 0:
        res += letter * (amt // 2)
    else:
        if odd:
            print("NO SOLUTION")
            exit()
        odd = letter * amt

print(res + odd + res[::-1])