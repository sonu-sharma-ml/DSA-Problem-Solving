class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def display(self):   # ✅ FIX: inside class
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")


# Driver code
linked_list = linkedlist()


linked_list.append(10)
linked_list.display()  # Output: 10 -> None
