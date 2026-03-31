# Explanation

**Difficulty**: `Medium`
**Time Complexity**: `O(N)`
**Space Complexity**: `O(1)`

## Approach

To delete a node from a doubly linked list, we need to:
1. Find the node to delete (by value)
2. Update the `prev` pointer of the next node to point to the node before the deleted node
3. Update the `next` pointer of the previous node to point to the node after the deleted node
4. Free the memory of the deleted node

### Edge Cases:
- **Delete head node**: Update head to head.next
- **Delete tail node**: Set previous node's next to None
- **Delete middle node**: Connect previous and next nodes
- **Node not found**: Return without changes
- **Single node list**: Set head to None
