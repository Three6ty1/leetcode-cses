# Stack

## Basic Principles
- Bro it's a stack.
- Use the last in, first out property
- Python deque type

### Valid Parenthesis
- Hashmap with open braces as keys and corresponding as values
- If its an open brace, append
- If not an open brace, check if the stack is empty (mismatch) and if the next pop is equivalent to the key
- If the stack is empty that means everything closed properly

### Min Stack
- Standard stack operations
- Keep track of the minimum of the stack using a tuple
    - Each tuple keeps track of the minimum of the stack including the value itself
    - For each addition assign the min in the tuple the min of the current stack min at stack[-1] or the val

### Evaluate Reverse Polish Notation
- If its a token, pop y first then pop x (since x + y would be right to left when popped out)
- Append the resulting operation to the stack
- In Python specifically, the upper value must be float(x) / y and then converted to int...
    - Dumb python things

### Generate Parenthesis
- DFS
    - Recurse through keeping track of the left, right and current string
- For the base case, realise that n is the amount of braces, and braces are paired therefore if len = n * 2 we 
submit the case and return the current string
- Left = open brace. If open braces < the max n braces, we can add more open braces
- Right = close brace. Close braces must be paired with open braces, therefore close < open means we can add more close braces
- Call dfs

### Daily Temperatures
- [Decreasing Monotonic Stack](https://leetcode.com/problems/daily-temperatures/solutions/1574808/c-python-3-simple-solutions-w-explanation-examples-images-2-monotonic-stack-approaches)
- "Thus, the pattern we see is that we **iterate forward till we find a warmer day** and that day will be the **answer for all elements before it that are cooler** (and not found a warmer day). Thus, we can maintain a stack consisting of indices of days which haven't found a warmer day."
- Store the indexes on the stack
- If one day is warmer than the last on the stack, that means every day in stack just met its warmer day
    - For that day in the stack in ans ans[stack[-1]] calculate the distance to the current day i - stack[-1]
    - Pop and move on

### Car Fleet
- First we sort the array from closest -> furthest away from destination
- This is because the cars ahead will always block the ones behind, therefore they are the limiting factor
    - For each car calculate the time it will take to get to the destination from that position
- A new fleet is created only when the next car is slower than the car infront, creating a gap
- If a car is faster than a car in front, then it catches up and forms a fleet with the car in front
- We keep track of the global maximum time


