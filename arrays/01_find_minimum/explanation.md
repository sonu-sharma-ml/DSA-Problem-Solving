# Explanation

**Difficulty**: `Easy`
**Time Complexity**: `O(N)`
**Space Complexity**: `O(1)`

## Approach
We iterate through the entire array exactly once. We keep track of the smallest element seen so far using a `min` variable initialized to infinity. Since we only use one variable for tracking, the space complexity is constant O(1), and time complexity is O(N) where N is the length of the array.
