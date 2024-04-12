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

### Longest Palindromic Substring
- Keep track of the index of the longest substring instead of the substring itself
- Start the palindrome calculation from every letter
- For every letter
    - Check for an odd palindrome by starting l and r from i
    - Check for an even palindrome by starting l from i and r from i + 1
    - Make sure to boundary check
    - Check if length of r - l is more than the max index
- Return spliced array at res_l res_r + 1

### Palindromic Substring
- The same as longest palindromic substring
- The if statement for a palindrome extends to the whole loop
- Every iteration of the loop means an additional substring is added
- Keep track of the amount in self.res

### Decode Ways
- Bottoms Up
- But instead of doing "steps" we're either considering numbers as 1 digits or 2 digits
- Hashmap for the dp. Base case of len(s) = 1
- Loop every digit from bottom up
    - If == 0, we assign it as 0 mappings as this depends on whether the next number exists or not
    - Then we treat it as a single digit/*step*, **we add onto d[i + 1]**
        - Since our base case is len(s) = 1, the first iteration will assign the single case letter as 1
    - The double case layers as a seperate if on single case
        - We can only double if i + 1 < len(s)
        - Check that i is either 1 or 2, if 2 then check if its 0-6
        - Then since this is "two" steps, **we add onto d[i + 2]**

### Coin Change
- Not bottoms up... I forgot the name of it
- Initialise dp array
    - [0] initial index, and inf * amt of coins to the target number
    - The dp array will store "the amount of coins it takes to get to that index
    - Each index is a coin amount
    - Therefore at index 5, we will get the minimum amount of coins that sum to $5
- Loop through amount + 1 (since first element is appended to 0)
    - For each coin, check if the sum of the current coin - the possible coins <= 0
    - Perform Dp operation
    - dp[i] = min(dp[i] (previous amount), dp[i - coin] + 1 (the amount to get to the previous sum + 1 for the current coin))
- Check if inf propagated to the end of the array, if so return - 1
- Return dp[-1]

### Maximum Product Subarray
- Sliding window esque dp solution
- Keep track of res
    - Initialise as max(nums) as the subarray could be size 1
- CurMin and CurMax
- Loop through all nums and calculate the curMax and curMin with max and min operations
    - n * curMin, n * curMax and n
    - Use temp variable to store old curMax
- res = max(res, curMax)
- This works because the n basically moves the subarray up once we find a better subarray
- Storing curMin means that we can find a case for -ve n

- The iterative solution
- Observations about negative numbers
    - Even negative numbers in array means the whole array is the maximal subarray
    - Odd negative numbers means that we have to exclude one of the negative numbers
        - We can do that by taking the subarrays to the left and right of the number
- We can then know that for some number k we can take the 0 to k - 1 subarray and the k + 1 - n subarray
- Since we don't know where this value is, we can do two passes, keeping track of the max value
- Because we have a case where 0 could be in the array, we can reset the product of the pass to 1.

### Word Break
- Word set of the dict
- Initialise dp to [False] * n + 1
- Since it's bottoms up, initialise dp[n] to True
- Loop -ve range
    - We loop through j = i + 1 to n + 1
    - The current characters were trying to get is i:j
    - The previous computed values are at dp[j]
    - If i:j is a valid word and dp[j] which is the rest of the array is a valid break
    - Then the array up to dp[i] is a valid break
    - *Break* out of the j loop since we've found a match for this index i
- As per usual, return dp[0] for bottoms up

### Longest Increasing Subsequence
- Initialise dp [1] * len
- Not bottoms up
- For i in nums
- For j in i, for every number between 0 - the current index
    - Find the longest increasing subsequence where nums[i] > nums[j] (strictly increasing)
    - When this is false, we assign dp[i] = max dp[i] and dp[j] + 1 since j will start from 0 and build the subsequence up to j
        - This is getting the maximum between the LIS that ends at dp[i] and the LIS at dp[j] + 1 including the current value
    - We continue doing from k - i since there might be an even longer subsequence than from 0 - k
- Return max(dp) since we arent keeping track of max in a res (slows down time too much)

### 01 Matrix
- 2 approaches
- BFS with queue
    - Initialise every index on the matrix
        - If 0, add to queue
        - Otherwise, mark as -1 to indicate unvisited
    - While the queue isn't empty
        - Pop from queue (first loop is starting from 0)
        - For each direction
        - Check for boundaries and check that this current location is -1 (not visited)
        - Assign the direction with the origin position + 1
        - Append this position to the queue
- Dynamic Programming
    - Only process the 1 cells
    - Since we can't dp on all 4 directions at a time due to not knowing if it was computed yet
    - We restrict from top-left to bottom-right and bottom-right to top-left
    - That means on the first pass, we calculate distance from the top and left adjacent cells + 1
    - On the second pass, we calculate distance from the bottom + 1 and right + 1 adjactent cells and get minimum compared to the first pass
