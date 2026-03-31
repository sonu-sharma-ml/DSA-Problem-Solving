"""
Problem Statement: Find the Middle of a Linked List (Counting)

Description:
Find the middle node of a linked list by first traversing the entire list to count nodes, then traversing again up to (count / 2).
"""

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

    def find_middle(self):
        if self.head is None:
            return None
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next
        middle = count // 2
        current_node = self.head
        for _ in range(middle):
            current_node = current_node.next
        return current_node.data



    def display(self):   # ✅ FIX: inside class
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Driver code
linked_list = linkedlist()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.append(50)
linked_list.append(60)
linked_list.append(70)
linked_list.append(80)
linked_list.append(90)
linked_list.append(100)
linked_list.display()
print("Middle element:", linked_list.find_middle())