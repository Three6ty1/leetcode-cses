# Arrays and Hashing

## Basic principles
- Use a hashmap for O(1) lookup times
  - Sets are implemented using hashmaps (Python)

## Kadane's Algorithm (Maximum Subarray)
- Initialise a local and global maximum to nums[0]
- Loop from 1 to len(nums)
- Local max = max(num, local_max + num)
- Global max = max(global max, local max)
- return global max

### Contains duplicate
- Compare lengths and return result
- Check if item in set O(1) and if not add to set O(1)

### Valid Anagram
- Have a hashmap increment letters for one string O(n) and decrement for the other O(n). Check if every letter entry == 0
- sort O(nlogn) and then compare results

### Two Sum
- A Complement hashmap that has the value as the key and the index as the value for O(n) look up times
  - For each element check if the target = curr + complement -> target - curr = complement exists using the hashmap lookup
  - It's okay if we loop past a number that has a solution because if the solution exists, the complement will see the first number that was added

### Group Anagrams
- Hashmap that has unique sorted keys.
  - For each new word O(n), sort it O(nlogn) and then insert/add it into the corresponding dict entry
  - At the end return the list of the Hashmap values

### Top K Frequent Elements
- Hashmap to count each value
  - Sort by the frequency using lambda function and reverse
  - Return the first k values using splicing
- Use counter to instantly create the hashmap
  - Use heapify with tuple of (freq, num) of the first [:k] elements
  - For the rest of n - k elements i.e. [k:] elements, heappushpop the rest of the numbers
  - Heapify will auto manage the most frequent
  - Return the numbers using list comprehension

### Product of Array Except Self
- Two arrays pre and suf
  - pre[i] = products num[j] <= i
  - suf[i] = products num[j] >= i
  - Then for each index of ans, we multiply the prefix product [i - 1] with the suffix product [i + 1] which is essentially getting the product excluding i
- Space O(n) approach
  - Use accumulate nums and mul for pre and then reverse the list [::-1] reverse again for suff
  - Get the answer with multiplication, using 1 if index is out of range
- Space O(1) (excluding output) approach
  - Init answer array with 1's since we're doing product
  - Since we skip each variable, we start curr at 1 and multiply ans[i] by curr. Then calculate the next curr by nums[i] to simulate "skipping" it
  - Do the same in reverse for suffix

### Valid Sudoku
- Loop through each square with i and j
  - Store a tuple each for the pair of (row index, val) (val, col index) these are switched to stop row and col from overlapping and the (row//3 col//3 val/) triple
  - Check if the size of set == size of the res

### Longest Consecutive Sequence
- Set for O(1) lookup
- Checking for x - 1 not in nums guarantees that we skip duplicates that don't have a streak
- Then we check for y = x + 1. While y is in our set, we increment to see if the next consecutive is there.
  - We then check the difference of y - x and get the maximum between this and the previousd

