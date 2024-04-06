# 1D Dynamic Programming

## Basic Principles
- I hate dynamic programming
- Bottoms up approach
    - Calculate the values from the end result
- 

### Climbing Stairs
- Since we can only climb 1 or 2 steps at a time, we'll start the base case at the start.
- [0, 0, 0, 0, 1, 1]
-  0  1  2  3  4  5
- From the end, it takes 1 action to get to the end of the staircase
- From the 3rd step, we can either take 1 step and end up at 4, or take 2 steps and end up at 5
    - Since we already know how many ways it takes to get from 4 and 5 to the top
    - We can add those two values and assign it to 3
- From 3, we can either take **one** or **two** steps
- [0, 0, 0, 0, 1, 1]
-  0  1  2  3  4  5
-           ^ one two
- temp = one
- one = one + two
- two = one
- From 2, we can either take **one** or **two** steps
- [0, 0, 0, 2, 1, 1]
-  0  1  2  3  4  5
-        ^ one two
- From 1, we can either take **one** or **two** steps
- [0, 0, 3, 2, 1, 1]
-  0  1  2  3  4  5
-     ^ one two
- Return one as it ends at the start of the stairs

### Min Cost Climbing Stairs
- Bottoms up bottoms up
- We append a 0 to the end of the min cost since having 2 steps from the 2nd last position shouldn't incur costs
    - This also avoids index out of range
- We start from len(n) - 1 ( - 2) and increment downwards
- [ a, b, c, d, e, 0]
-            ^ one two
- From d, we get the minimum of (e, 0) which is the same as saying taking one or two steps but choosing the cheapest
- Add that onto the cost of d
- Then return the minimum of starting at [0] or [1]

### House Robber
- Bottoms Up
- Append a 0 at the end, so that we can calculate without worrying about index
- [ a, b, c, d, e, 0 ]
-            ^  r1 r2
- If we rob d we can't rob r1 = n + 1, but we rob d + r2 = n + 2
- The decision to rob at d at index i is
    - Get the max between robbing d and not robbing d
    - nums[i] = max(nums[i] + nums[i + 2], nums[i + 1])
- Just like climbing stairs, return max of nums[0] and nums[1]

### House Robber 2
- The same solution as the previous
- Need to check for empty array
- Need to check for singular entry
- The trick is to call House Robber one on [1:] and [:-1]
    - The restrictions basically form a cycle array
    - If we do the first element, we cant do the last
    - If we do the last element, we cant do the first
    - Therefore we just exclude these elements in consideration

