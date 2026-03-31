"""
Problem Statement: Search Insert Position

Description:
Given a sorted array and a target value, find the index where the target should be inserted to maintain the sorted order.
"""

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