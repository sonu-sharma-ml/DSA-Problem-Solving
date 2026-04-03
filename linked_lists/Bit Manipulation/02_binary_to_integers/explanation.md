# Explanation

**Difficulty**: `Easy`
**Time Complexity**: `O(n)`
**Space Complexity**: `O(1)`

## Approach
The algorithm converts a binary string to an integer by iterating from right to left (least significant bit to most significant bit). For each '1' bit encountered, it adds 2^position to the result, where position starts at 0 for the rightmost bit and increments with each step. This builds the integer value by summing the values of all set bits.