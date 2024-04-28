# Sliding Window

## Basic Principles
- lo and hi
- Always want to loop across every possible value, which usually means when **hi** reaches the end
- Calculate the value
- Move up either lo or hi.
  - When the list has duplicates, make sure lo[i] != lo[i - 1]
- When using a map
  - For the starting position, remove its value and increment when the condition **is not satisfied**
  - Increment the hi via for loop in range or within the satisfied branch

### Best Time to Buy and Sell Stock
- Keep track of max
- If lo < hi, that means there is a profit
  - Calculate max between max and this profit
- Otherwise, hi < lo which means that there could be an even larger difference somewhere in the list
  - lo = hi
- Always increment hi

### Longest Substring Without Repeating Characters
- Keep track of max len as well as a set of seen characters
- lo keeps track of the start of the substring
- hi keeps track of the current character
- If hi is not in the set of seen, add it to the set, get max between seen and max, compare next character
- Otherwise remove the first character at lo, and increment lo to the next character

### Longest Repeating Character Replacement
- hi reaches end loop
- Keep track of max and a map of the characters
- Calculate the length of the current substring
- Get the maximum value in the character map
  - The maximum value is the most common character
  - That means curr_len - max(charMap.values()) will be equal to the letters that need to be replaced
  - If it is within or equal to the amount of operations we can update max

### Permutation in String
- Is s1 in s2?
- Base case if len(s1) > len(s2) we return False
- Get a map of the Counter of characters in s1
- Keep track of a dict of the charMap
- Before shifting, check if the charMap built from prev iter is equal to the Counter
- The sliding window should be of len(s1)
  - Shift only when this is true
  - Decrement the charMap[s2[lo]]
  - Remove it if the entry == 0
  - Increment lo

### Minimum Window Substring
- Increase r until we have all chars in t
- Decrease l to minimise the window while maintaining all chars in t
  - Increment l to force revaluation
  - Increment r always to look at next char
- Edge case for len(t) > len(s)
- Counter for t
- l, r and missing at len(t)
- Min_start and min_length init as len(s) + 1. We check this at the end for invalid input
- While < len(s)
  - If s[r] in the t_counter and the counter for the letter we want to find is > 0, we decrement the missing value
    - Also decrement the counter
  - While we have 0 missing values
    - Update the minimum window with **r - l + 1** and min_length
    - If the s[l] is a char in t, we increment its t_count
    - If the t_count is now more than 0, we now dont have t in the current window, increment the missing value
    - Always increment l
- Check if the min_length hasnt changed from len(t) + 1

### Trapping Rain Water
- The other way for this question is the DP solution
- Initialise left and right max to either ends
- Set l and r to 1 and n - 2
- While l <= r
- Set the left and right max to the max of the current l and max and current r and max respectively
- If else to check if either left or right is smaller
  - The smaller maximum gets added to the total using l/r_max - height[l/r]
  - Increment/Decrement respectively
  