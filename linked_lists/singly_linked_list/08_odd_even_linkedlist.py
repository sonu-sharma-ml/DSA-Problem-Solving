"""
Problem Statement: Odd Even Linked List Logic

Description:
Group all odd-indexed nodes together followed by the even-indexed nodes using an array concatenation approach.
"""

class Node:
    def __init__(self, value):  # ✅ Added __init__
        self.value = value
        self.next = None


class LinkedList:  # ✅ Fixed spelling (Linkedlist → LinkedList)
    def __init__(self):  # ✅ Added __init__
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
        slow = self.head
        fast = self.head.next
        store1 = []
        store2 = []
        store = []
        while fast is not None and fast.next is not None:
            store1.append(slow.value)
            store2.append(fast.value)
            slow = slow.next.next
            fast = fast.next.next
        store1.append(slow.value)
        store2.append(fast.value)
        store = store1 + store2[::-1]
        print(store)
        current_node = self.head
        for i in range(len(store)):
            current_node.value = store[i]
            current_node = current_node.next


        while fast is not None and fast.next is not None:
            store.add(slow)

        print(store[0])





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

ll.display()

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

ll.arrange()