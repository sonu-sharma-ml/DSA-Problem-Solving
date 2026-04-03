# Explanation

**Difficulty**: `Easy`
**Time Complexity**: `O(log n)`
**Space Complexity**: `O(log n)`

## Approach
The algorithm converts an integer to binary by repeatedly dividing the number by 2 and collecting the remainders. Each remainder (0 or 1) represents a bit in the binary representation. The process continues until the quotient becomes 0. Finally, the collected bits are reversed to get the correct binary order.