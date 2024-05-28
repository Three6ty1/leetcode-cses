"""
https://www.geeksforgeeks.org/cses-solutions-gray-code/
"""

n = int(input())

def recursive(n: int) -> list:
    if n == 1:
        return ["0", "1"]
    
    code = recursive(n - 1)
    r_code = code[::-1]

    for i in range(len(code)):
        # e.g. {00, 01} and {10, 11}
        # if we flip the second list
        # {00, 01} {11, 10}
        # we can see that the old ends of the list now differ by 1

        # for each code prepend 0
        code[i] = "0" + code[i]

        # for each code in the prepend 1
        code.append("1" + r_code[i])

    return code

for code in recursive(n):
    print(code)
