"""
Problem Statement: Find the Minimum Element in an Array

Description:
Given an array of numbers, iterate through it to find and return the smallest (minimum) value.
"""

nums = [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
min = float('inf')
for i in range(len(nums)):
    if nums[i] < min:
        min = nums[i]
print(min)