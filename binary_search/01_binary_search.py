# You are given a sorted array nums and a target value.
# Return the index of the target if it exists; otherwise return -1.
# The algorithm must run in O(log n) time.


nums = [12,1,2,12,23,34,45,67]
nums.sort()
print(nums)


def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

result = binary_search(nums, 23)
print(result)