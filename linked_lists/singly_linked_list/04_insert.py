"""
Problem Statement: Insert Node at Specific Position

Description:
Implement a function to dynamically insert a new node at an arbitrary 0-indexed position within a singly linked list.
"""

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

        

    # def insert_at_beginning(self, data):
    #     new_node = Node(data)
    #     new_node.next = self.head
    #     self.head = new_node



    # def insert_at_end(self, data):
    #     new_node = Node(data)
    #     if self.head is None:
    #         self.head = new_node
    #         return
    #     temp = self.head
    #     while temp.next is not None:
    #         temp = temp.next
    #     temp.next = new_node

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        for _ in range(position - 1):
            if temp is None:
                raise IndexError("Position out of bounds")
            temp = temp.next
        if temp is None:
            raise IndexError("Position out of bounds")
        new_node.next = temp.next
        temp.next = new_node

    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Driver code
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.insert_at_position(25, 2)
linked_list.display()  # Output: 10 -> 20 -> 25 -> 30 -> 40 -> None