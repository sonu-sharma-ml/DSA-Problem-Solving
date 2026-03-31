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
    # METHOD 1: Reverse using STACK
    # -------------------------------
    def reverse_stack(self):
        if self.head is None:
            return

        temp = self.head
        stack = []

        # Store all values
        while temp is not None:
            stack.append(temp.val)
            temp = temp.next

        # Replace values
        temp = self.head
        while temp is not None:
            temp.val = stack.pop()
            temp = temp.next

    # ------------------------------------
    # METHOD 2: Reverse using POINTERS ⭐
    # ------------------------------------
    def reverse(self):
        temp = None
        current = self.head

        # Swap next and prev for each node
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        # Update head
        if temp is not None:
            self.head = temp.prev

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

dll.insert_at_head(12)
dll.insert_at_head(23)
dll.insert_at_head(32)
dll.insert_at_head(44)
dll.insert_at_head(54)
dll.insert_at_head(65)
dll.insert_at_head(76)
dll.insert_at_head(87)
dll.insert_at_head(98)

print("Original List:")
dll.display()

print("\nReverse using STACK:")
dll.reverse_stack()
dll.display()

print("\nReverse using POINTERS:")
dll.reverse()
dll.display()