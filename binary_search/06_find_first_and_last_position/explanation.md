# Explanation

**Difficulty**: `Medium`
**Time Complexity**: `O(N) / O(log N)`
**Space Complexity**: `O(1)`

## Approach
The provided solution implements a linear scan O(N) algorithm that updates `start` only once and continuously cascades `end`. An optimal solution would replace this loop with two separate Binary Searches (one for the first occurrence, another for the last).
