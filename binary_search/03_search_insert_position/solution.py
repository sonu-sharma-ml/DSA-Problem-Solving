nums = [1,3,5,7,9,11,13,15,17,19]
low = 0
high = len(nums) - 1
target = 10

while low <= high:
    mid = low + (high - low) // 2

    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print(low)