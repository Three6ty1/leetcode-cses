n = int(input())
nums = [int(nums) for nums in input().split(" ")]

moves = 0
for i in range(1, n):
    diff = nums[i - 1] - nums[i]
    
    if diff > 0:
        moves += diff
        nums[i] += diff

print(moves)