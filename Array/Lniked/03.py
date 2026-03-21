class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def create_list(self , data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node


    def insert_at_beginning(self ,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return

link_list = LinkedList()
link_list.create_list(10)
link_list.create_list(20)
link_list.create_list(30)
print(link_list.head.data)  # Output: 10
print(link_list.head.next.data)  # Output: 20
print(link_list.head.next.next.data)  # Output: 30
link_list.insert_at_beginning(5)
print(link_list.head.data)  # Output: 5
print(link_list.head.next.data)  # Output: 10   