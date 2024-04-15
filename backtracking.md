# Backtracking

## Basic Principles
- DFS
- Start from 0 and then until we reach the end of the decision tree
    - Go down a path where we add the current value
    - Revert that change
    - Which causes us to go down the path without that value
- It is basically bruteforcing

### Subsets
- Have a subset
- dfs(i) where i = 0 initially
- i keeps track of the amount of decisions we made
    - If we've made the same amount of decisions of len(nums)
    - We must have reached the end of the add or not add decision tree
    - Add this subset
- Append nums[i] to subset and recursively call dfs
- Remove nums[i] then recursively call dfs

- The other way
- dfs(nums, path)
- For each recursive call
    - We append the current path onto the result because we're looking for the power set
    - For each num remaining in nums
    - We recursively call dfs(nums[i + 1:]) and then append the current nums[i] onto path

### Combination Sum
- dfs(nums, target, path)
- Every path we take we call dfs nums[i:], target - nums[i] and appaend the current nums[i] onto path
    - This is crucially nums[i:] because we can infinitely use the current num
- This is the same pattern

### Permutations
- dfs(nums, path)
- When nums is exhausted we return
- The main trick is that during our for loop call
    - We pass in nums[:i] + nums[i + 1:]
    - What this does is that we removed the number at i and passed in the rest of the array
    - path updates as usual path + [nums[i]]

### Subsets 2
- Sort nums
- Same as Subsets 1
    - In the for loop
        - if i > 0 and nums[i] == nums[i - 1]
        - continue
    - This avoids all duplicate numbers

### Combination Sum 2
- Sort nums again
- The same as Combination Sum 1
    - Just need the if statement in the middle of the loop to avoid duplicates

### Word Search
- Do preliminary checks on 
    - len(word) > len(rows) * len(cols)
    - Counter(sum(board, [])) is more than Counter(word).items()
- Use a seen set of (row, col) location tuples to keep track of dfs path
- dfs(row, col, i)
- We only traverse on letters that are in the word
- Check for row col out of index, check for row col in seen, check for board[row][col] matches letter
- If we pass the checks, **backtrack** on the adjacent 4 tiles.
    - Add to seen,
    - Call dfs on all 4 sides
    - Remove from seen
    - return res 
- Call dfs starting from every position of i, j row col

### Palindrome Partitioning
- The same format, but
    - For loop needs to start with + 1 for the splicing to work properly since its exclusive
    - Or we can manually add + 1 to every i
    - Check if the substring of s from s[:i] is a palindrome through string reversal s[:i][::-1]
    - If it is, call dfs on s[i:], and path + [s[i:]] instead of i + 1

### Letter Combinations of a Phone Number
- Standard backtracking
- For each number of the current mapping of the letter,
    - Recursively call dfs(digits[1:], path + letter)
