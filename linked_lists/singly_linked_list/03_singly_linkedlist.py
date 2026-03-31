class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self , data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ->")
            temp = temp.next
        print("None")

# Driver code
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.display()  # Output: 10 -> None
