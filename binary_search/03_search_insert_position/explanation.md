# Explanation

**Difficulty**: `Easy`
**Time Complexity**: `O(log N)`
**Space Complexity**: `O(1)`

## Approach
We modify the standard binary search to find exactly where a target belongs. If the target is not found in the array, the `low` pointer at the end of the while loop will always rest precisely at the index where the missing target should be linearly inserted to maintain sorting.
