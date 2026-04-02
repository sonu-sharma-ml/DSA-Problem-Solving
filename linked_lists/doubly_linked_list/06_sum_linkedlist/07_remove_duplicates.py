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
    # REMOVE DUPLICATES ⭐
    # -------------------------------
    def remove_duplicates(self):
        """
        Remove duplicate nodes from the doubly linked list.
        Keeps the first occurrence of each value.
        """
        seen = set()
        temp = self.head

        while temp is not None:
            if temp.val in seen:
                # Remove this duplicate node
                temp.prev.next = temp.next
                if temp.next is not None:
                    temp.next.prev = temp.prev
            else:
                seen.add(temp.val)
            temp = temp.next

    # Display list
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.val, end=" <-> ")
            temp = temp.next
        print("None")


# -------------------------------
# DRIVER CODE
# -------------------------------
dll = DoublyLinkedList()

dll.insert_at_head(2)
dll.insert_at_head(9)
dll.insert_at_head(2)
dll.insert_at_head(4)
dll.insert_at_head(6)
dll.insert_at_head(2)
dll.insert_at_head(4)
dll.insert_at_head(3)
dll.insert_at_head(2)

print("Original List:")
dll.display()

print("\nAfter Removing Duplicates:")
dll.remove_duplicates()
dll.display()