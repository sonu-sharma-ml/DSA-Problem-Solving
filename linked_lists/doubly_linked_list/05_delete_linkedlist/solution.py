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
    # DELETE A NODE BY VALUE ⭐
    # -------------------------------
    def delete_node(self, key):
        temp = self.head

        # Search for the node with the given key
        while temp is not None:
            if temp.val == key:
                break
            temp = temp.next

        # If node not found
        if temp is None:
            print(f"Node with value {key} not found!")
            return

        # Case 1: Delete head node
        if temp == self.head:
            self.head = temp.next
            if self.head is not None:
                self.head.prev = None

        # Case 2: Delete tail node
        elif temp.next is None:
            if temp.prev is not None:
                temp.prev.next = None

        # Case 3: Delete middle node
        else:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev

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

print("\nDelete node with value 44:")
dll.delete_node(44)
dll.display()

print("\nDelete head node (98):")
dll.delete_node(98)
dll.display()

print("\nDelete non-existent node (100):")
dll.delete_node(100)
dll.display()
