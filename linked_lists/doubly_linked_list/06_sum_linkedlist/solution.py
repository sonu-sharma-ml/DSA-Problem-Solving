class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at head
    def insert_at_head(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # -------------------------------
    # FIND SUM OF PAIRS ⭐
    # -------------------------------
    def find_pairs_with_sum(self, target_sum):
        """
        Find all pairs of nodes whose sum equals target_sum.
        Returns the count of such pairs.
        """
        temp1 = self.head
        count = 0

        # Traverse through each node
        while temp1 is not None:
            temp2 = temp1.next
            # Check pairs with subsequent nodes
            while temp2 is not None:
                if temp1.val + temp2.val == target_sum:
                    print(f"{temp1.val} + {temp2.val} = {target_sum}")
                    count += 1
                temp2 = temp2.next
            temp1 = temp1.next

        return count

    # Display list
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.val, end=" <-> ")
            temp = temp.next
        print()


# -------------------------------
# DRIVER CODE
# -------------------------------
dll = DoublyLinkedList()

dll.insert_at_head(10)
dll.insert_at_head(9)
dll.insert_at_head(8)
dll.insert_at_head(7)
dll.insert_at_head(6)
dll.insert_at_head(5)
dll.insert_at_head(4)
dll.insert_at_head(3)
dll.insert_at_head(2)

print("Original List:")
dll.display()

print("\nFinding pairs with sum = 9:")
result = dll.find_pairs_with_sum(9)
print(f"Total pairs found: {result}")