# Explanation

**Difficulty**: `Medium`
**Time Complexity**: `O(log N)`
**Space Complexity**: `O(1)`

## Approach
We apply binary search by identifying which side of `mid` is perfectly sorted. Once we establish the sorted side, we simply check whether our target falls inside that sorted range. If it does, we narrow bounds to that range, otherwise, we search the unsorted half.
