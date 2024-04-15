# Binary Search

## Basic Principles
- lo is always 0 and hi is the **range of all possible solutions** (sometimes n - 1 or n for insertion)
- Loop is while the lo and hi dont intersect
- **If we don't know the target value**, we need to have <=, compare mid == target and skip mid in both lo and hi

- **EXCLUDE MIDDLE** on one side!!
- If + 1, its upper middle
  - hi should - 1 and **exclude middle**
- If just hi - lo, its lower middle
  - lo should + 1 and **exclude middle**
- The first check is always if target < nums[mid] or target > nums[mid]
  - Opposite to two pointers!!!
- If more than move the lo pointer up to mid (+ 1)
- If less than move the hi pointer down to mid (-1)
- Return nums[lo] if target

## Alternate version
- lo <= hi
- target == mid
- lo = mid + 1
- hi = mid - 1

### Search a 2D Matrix
- Normal binary search target ver
- The range is of row_num * col_num - 1
  - Main array = row, Subarray is col
- Calculate the mid value by having [mid / col_num] [mid % col_num]
- This is practically the reverse of the initial mid calculation

### Koko Eating Bananas
- Core concept, lo hi is initialised to the range of eating
  - lo = atleast 1 banana
  - hi = at most the biggest banana pile max(piles)
- We change the max based on whether koko can afford to eat less bananas or not.
  - Sum up the days needed to eat each pile of the bananas
  - If the time it takes to eat all the bananas at the current rate mid, we need to increase lo
    - i.e. if target > nums[mid]
    - sum of ( pile + mid - 1 / mid for pile in piles ) more than total time
    - hi = mid
- return lo as original ver

### Find Minimum in Rotated Array
- Normal binary search but just like before, the target matching is changed
- We are trying to find min
- If nums[mid] > nums[right] that means we know the loop must have happened somewhere on the left
  - Move left up
- If otherwise nums[mid] <= nums[right] because nums[right] is consistently increasing from mid
  - We don't do right = mid - 1 because we're not sure if this is the min yet.

### Time Based Key-value store
- Hashmap that stores map[key] with an array of (value, timestamp) tuples
- If the timestamp matches index [1] in tuple, return value
- If we don't find timestamp in the array
  - If the resulting hi timestamp is lte the timestamp, i.e. this was the most recent timestamp, we return it
  - Otherwise, there has been no previous timestamp, return "" 

### Search in Rotated Sorted Array
- lo = 0, hi = len(nums) and lo < hi
- Two halves
  - Find whether the target is in the rotated section or normal section of the array
  - Normal [4 5 6] [1 2 3] Rotated
  - Normal case
    - target >= nums[0] > nums[mid]
    - [4 5 6] [1 2 3]
    -      t   m
    - hi = mid
  - Rotated case
    - target < nums[0] < nums[mid]
    - [4 5 6] [1 2 3] 
    -      m   t
    - lo = mid
- The rest of the half of logic is normal binary sort
- Exiting when mid == target
