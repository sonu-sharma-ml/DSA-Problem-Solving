# Explanation

**Difficulty**: `Easy`
**Time Complexity**: `O(log N)`
**Space Complexity**: `O(1)`

## Approach
Standard binary search implementation. We use two pointers, `left` and `right`, to continually halve the search space containing the target value by determining if the target is greater or smaller than the `mid` element. The array must be sorted for this to work.
