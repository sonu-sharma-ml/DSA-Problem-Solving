# Explanation

**Difficulty**: `Easy`
**Time Complexity**: `O(1)`
**Space Complexity**: `O(1)`

## Approach
To insert at head, we securely tie the new node's `next` to the current head, map the current head's `prev` directly to the new node, and then simply reassign the head pointer.
