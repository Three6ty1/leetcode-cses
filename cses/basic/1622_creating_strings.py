string = str(input())

res = set()

def recursive(letters, path):
    if not letters:
        res.add(path)

    for i in range(len(letters)):
        recursive(letters[:i] + letters[i + 1:], path + letters[i])

string = sorted(list(string))

recursive(string, "")
print(len(res))
for perm in sorted(res):
    print(perm)