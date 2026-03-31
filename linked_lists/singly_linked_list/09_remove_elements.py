"""
Problem Statement: Remove Elements by Target Value

Description:
Traverse a singly linked list and remove the first occurrence of a specific targeted value.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

    # ✅ REMOVE BY VALUE
    def remove(self, value):
        current = self.head
        prev = None

        # Case 1: head node
        if current is not None and current.value == value:
            self.head = current.next
            return

        # Traverse
        while current is not None:
            if current.value == value:
                break
            prev = current
            current = current.next

        # Value not found
        if current is None:
            print("Value not found")
            return

        # Remove node
        prev.next = current.next

    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")