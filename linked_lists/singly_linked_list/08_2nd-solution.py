"""
Problem Statement: Odd Even Array Positions of Linked List

Description:
Rearrange a linked list values sequentially by gathering alternating values (from odd indices, then even indices) dynamically mapping them back to the sequential list.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
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

    def arrange(self):
        """Rearrange: odd positions first, then even positions"""
        if not self.head:
            return
        
        # Step 1: Collect odd position values (1st, 3rd, 5th...)
        temp = self.head
        store = []
        while temp and temp.next:
            store.append(temp.value)
            temp = temp.next.next
        
        # Add last odd position if exists
        if temp:
            store.append(temp.value)
        
        print(f"Odd positions: {store}")
        
        # Step 2: Collect even position values (2nd, 4th, 6th...)
        temp = self.head.next  # Start from 2nd node
        while temp and temp.next:
            store.append(temp.value)
            temp = temp.next.next
        
        # Add last even position if exists
        if temp:
            store.append(temp.value)
        
        print(f"Final arrangement: {store}")
        
        # Step 3: Update linked list with new arrangement
        temp = self.head
        for i in range(len(store)):
            temp.value = store[i]
            temp = temp.next

    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")


# Test
ll = LinkedList()
ll.append(10)   
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
ll.append(60)   
ll.append(70)   
ll.append(80)
ll.append(90)
ll.append(100)

print("Original:")
ll.display()

print("\n" + "@"*50 + "\n")

ll.arrange()

print("\nAfter arrange:")
ll.display()