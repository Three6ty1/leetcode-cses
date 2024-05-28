"""
https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/
"""
from collections import deque

n = int(input())
steps = []

def recursive(n, from_stack, to_stack, aux_stack):
    global steps
    if n == 0:
        return
    recursive(n - 1, from_stack, aux_stack, to_stack)
    steps.append(from_stack + " " + to_stack)
    recursive(n - 1, aux_stack, to_stack, from_stack)

recursive(n, "1", "3", "2")
print(len(steps))
print("\n".join(steps))