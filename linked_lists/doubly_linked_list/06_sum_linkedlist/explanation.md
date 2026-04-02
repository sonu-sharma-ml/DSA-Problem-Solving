# Explanation

**Difficulty**: `Medium`
**Time Complexity**: `O(N²)`
**Space Complexity**: `O(1)`

## Approach

To find all pairs of nodes whose sum equals the target value:

1. **Two-pointer approach**: Use two pointers to traverse the list
2. For each node, iterate through all remaining nodes to find pairs
3. Count pairs where the sum equals the target

### Algorithm:
1. Initialize a pointer at the head (temp1)
2. For each node, use another pointer (temp2) to traverse subsequent nodes
3. Check if current node values sum to target
4. Increment count for each valid pair

### Edge Cases:
- **Empty list**: Return 0
- **Single node**: No pairs possible, return 0
- **No valid pairs**: Return 0
- **All pairs valid**: Count all combinations