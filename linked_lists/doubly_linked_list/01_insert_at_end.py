class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def dis(self):
        temp = self.head
        while temp is not None:
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
dll.insert_at_end(6)

dll.dis()
print("++++++++++++++++++++++")

dll.insert_at_end(7)
dll.dis()