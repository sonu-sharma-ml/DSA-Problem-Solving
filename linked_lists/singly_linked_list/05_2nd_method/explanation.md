# Explanation

**Difficulty**: `Easy`
**Time Complexity**: `O(N)`
**Space Complexity**: `O(1)`

## Approach
We deploy Floyd's cycle-finding (Tortoise and Hare algorithm). Using two pointers moving from the initial head, the `fast` jumps twice as quickly as `slow`, automatically landing the `slow` strictly at the structural middle when `fast` breaks bounds.
