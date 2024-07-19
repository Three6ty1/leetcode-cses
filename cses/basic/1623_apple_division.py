n = int(input())
apples = [int(x) for x in input().split(" ")]

def recursive(arr, sum1, sum2):
    if not arr:
        return abs(sum1 - sum2)
    
    choose = recursive(arr[1:], sum1 + arr[0], sum2)
    not_choose = recursive(arr[1:], sum1, sum2 + arr[0])

    return min(choose, not_choose)

print(recursive(apples, 0, 0))