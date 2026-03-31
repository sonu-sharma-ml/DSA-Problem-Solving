# Explanation

**Difficulty**: `Medium`
**Time Complexity**: `O(N)`
**Space Complexity**: `O(1)`

## Approach
Relies on a structural tracking counter to reach a specific 0-indexed position manually resolving ties `new_node.next = temp.next` and securing `temp.next = new_node` sequentially without detaching the sequence tail.
