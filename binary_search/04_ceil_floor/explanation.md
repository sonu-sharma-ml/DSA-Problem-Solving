# Explanation

**Difficulty**: `Medium`
**Time Complexity**: `O(log N)`
**Space Complexity**: `O(1)`

## Approach
Using binary search, if the `target` is not perfectly matched, we adapt our bounds conditionally. Whatever the final closest lesser boundary rests on becomes the 'Floor', and the closest greater boundary becomes the 'Ceil' value.
