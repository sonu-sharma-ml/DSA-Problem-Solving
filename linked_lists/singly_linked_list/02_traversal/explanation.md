# Explanation

**Difficulty**: `Easy`
**Time Complexity**: `O(N)`
**Space Complexity**: `O(1)`

## Approach
Moves sequentially along the linked list utilizing `current = current.next` structure safely iterating until `None` indicates the tail, whilst capturing the local node value.
