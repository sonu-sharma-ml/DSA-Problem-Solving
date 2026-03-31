"""
Problem Statement: Traverse and Print a Singly Linked List

Description:
Implement a method to iterate (traverse) through all nodes from the head to the tail and print their values sequentially.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traversal(self):
        if self.head is None:
            print("Linked list is empty")
            return
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.data, end=" -> ")
                current_node = current_node.next
            print("None")


link_list = LinkedList()
link_list.head = Node(10)
link_list.traversal()  # Output: 10 -> None