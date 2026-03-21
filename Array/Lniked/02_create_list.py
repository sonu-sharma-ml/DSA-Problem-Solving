class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None


    def create_list(self , data ):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

link_list = LinkedList()
link_list.create_list(10)
link_list.create_list(20)
link_list.create_list(30)
link_list.create_list(40)
link_list.create_list(50)
link_list.create_list(60)
link_list.create_list(70)
link_list.create_list(80)
link_list.create_list(90)
link_list.create_list(100)
print(link_list.head.data)  # Output: 10
print(link_list.head.next.data)  # Output: 20   

