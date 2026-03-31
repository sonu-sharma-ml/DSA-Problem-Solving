"""
Problem Statement: Remove Nth Node from End

Description:
Locate and remove an elements sequence dynamically from the linked list by fast-forwarding an end pointer gap.
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

    def remove():
        slow = self.head
        fast = self.head
        while _ in range(n):
            fast = fast.next
        if fast == None:
            self.head = self.head.next
            return
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return self.head


    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")