class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # ✅ insert at end (needed)
    def insert_at_end(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # ✅ insert at position
    def insert_at_position(self, val, position):
        new_node = Node(val)

        # Case 1: insert at head
        if position == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return   # ✅ IMPORTANT

        current = self.head
        count = 0

        # move to position-1
        while current is not None and count < position - 1:
            current = current.next
            count += 1

        if current is None:
            print("Invalid position")
            return

        # insert node
        new_node.next = current.next
        new_node.prev = current

        if current.next:
            current.next.prev = new_node

        current.next = new_node

    def dis(self):
        temp = self.head
        while temp:
            print(temp.val, end=" _>_ ")
            temp = temp.next
        print()


# Driver code
dll = DoublyLinkedList()

dll.insert_at_end(1)
dll.insert_at_end(2)
dll.insert_at_end(3)
dll.insert_at_end(4)
dll.insert_at_end(5)

dll.dis()
print("++++++++++++++++++++++")

dll.insert_at_position(100, 2)
dll.dis()

dll.insert_at_position(200, 0)
dll.dis()