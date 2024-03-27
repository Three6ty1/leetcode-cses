# Two Pointers

## Basic Principles
- Left and Right pointers (l and r, lo and hi)
- We stop when the right pointer reaches the end
- The left pointer either moves up by one or moves up to the current right based on the condition
    - Keep track of existing results in a set or hashmap

### Valid Palindrome
- Two Pointers
    - l = 0, r = n
    - While true, return early if false, increment left and decrement right seperately until both are alphanumeric 
    numbers.
    - Compare if they are the same
- List reversal
    - Filter alnum on both and reverse one of the strings
    - String comparison

### Two Sum
- Smaller sums are on the left of the array
- **L**ess target, move **l**eft
- Larger sums are on the right of the array
- Mo**r**e target, move **r**ight
- Start from left and right and compare to target

### Three Sum (To 0)
- Sort numbers
    - Smaller sums i.e. negative are on the left
    - Larger sums i.e. positive are on the right
- Iterate through nums
    - l = i + 1, r = n - 1
    - While iterating, check the sum of num[i] and num[i + 1] and num[n - 1]
    - If **l**ess target, move **l**eft up
    - If more target, move right down
- While loop until l and r are not duplicates of their previous
- Increment once more.

### Container with Most Water
- The theory is going from max width and only incrementing on the max height guarantees that we find the maximum area.
- Keep track of maximum
- Start l r from 0 and n - 1
    - Increment the smaller height[r] or height[r]
