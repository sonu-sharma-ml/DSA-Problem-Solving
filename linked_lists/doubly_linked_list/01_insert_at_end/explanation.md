# Explanation

**Difficulty**: `Easy`
**Time Complexity**: `O(N)`
**Space Complexity**: `O(1)`

## Approach
We iterate through the `next` references until we reach the tail node. We then link our new node securely by patching `tail.next = new_node` and `new_node.prev = tail`.
