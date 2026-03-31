"""
Problem Statement: Find First and Last Position of Element in Sorted Array

Description:
Given a sorted array and a target value, find the starting and ending index position of the given target value.
"""

nums = [1,2,2,3,4,5,6,6,6,6,7,7,7,7,78,78,78,78,79,79,79,79]
target = 6

start = -1
end = -1

for i in range(len(nums)):
    if nums[i] == target:
        if start == -1:
            start = i
        end = i

print(start, end)