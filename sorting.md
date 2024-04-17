# Sorting Algorithms

### Sort Colors
- Dutch National Flag problem
- Two pass solution
    - start lo hi from whole array
        - Move hi down until nums[hi] != 2
        - If the current nums[lo] == 2, swap it with nums[hi] and increment hi
        - Akways increment lo
    - Start lo from 0 and leave hi
        - Move hi down until nums[hi] < 1 since 2 is already sorted, and all remaining 1's are sorted
        - Same if logic as above
- One pass solution (Dutch National Flag)
    - Partition the array into 4 regions
        - lo, mid, hi = 0, 0, n - 1
        - Below lo is 0
        - lo - mid is 1
        - mid - hi is unsorted
        - Above hi is 2
    - While mid <= hi (the unsorted section)
        - If the nums[mid] == 0, we move it below lo and increment mid and lo
        - If nums[mid] == 1, we increment mid since its already in sorted order (between lo - mid)
        - If nums[mid] == 2, we move mid to nums[hi] and **decrement hi**
            - We do not increment mid because the swap returns an unknown element
