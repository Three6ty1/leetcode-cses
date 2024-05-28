string = input()

longest = 1
curr = 1

for i in range(1, len(string)):
    if string[i] == string[i-1]:
        curr += 1

        if curr > longest:
            longest = curr
        
    else:
        curr = 1
    
print(longest)