"""
Problem Statement: Manual Node Linking Demonstration

Description:
Manually instantiate node objects and link them sequentially, then print their distinct node.next chained values to demonstrate references.
"""

class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
c1 = Node(10)
c2 = Node(20)
c3 = Node(30)
c4 = Node(40)
c1.next = c2
c2.next = c3
c3.next = c4
print(c1.data)
print(c1.next.data)
print(c1.next.next.data)
print(c3.next.data)