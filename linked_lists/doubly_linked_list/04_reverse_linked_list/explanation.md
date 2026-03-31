# Explanation

**Difficulty**: `Medium`
**Time Complexity**: `O(N)`
**Space Complexity**: `O(1) / O(N)`

## Approach
Two solutions are provided. Iterative mapping reverses the list optimally in-place by swapping the `next` and `prev` pointers concurrently for every node navigated. The secondary approach inefficiently loads values into a Stack O(N) space and manually writes them back entirely.
