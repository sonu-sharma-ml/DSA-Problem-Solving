# Explanation

**Difficulty**: `Medium`
**Time Complexity**: `O(N)`
**Space Complexity**: `O(1)`

## Approach
We first traverse forward using a counter until we arrive at `position - 1`. We then interweave the pointers by resolving `next` and `prev` ties of both adjacent bordering nodes to embrace the inserted new node internally.
