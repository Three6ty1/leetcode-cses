"""
https://www.geeksforgeeks.org/cses-solutions-trailing-zeros/
"""
n = int(input())

def solve(N):
    if N == 0:
        return 0
    
    # We recursively count (and take away at the same time) the factors of 5 in N. using the property where N! is 1 * 2 * 3 *etc
    return N // 5 + solve(N // 5)

print(solve(n))