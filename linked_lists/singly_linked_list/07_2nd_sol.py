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


    def cheak_loop(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False



    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")



ll = Linkedlist()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(10)
ll.append(60)
ll.append(70)
ll.append(80)
ll.append(90)
ll.append(100)

ll.display()
print("-------------------------")
print(ll.cheak_loop())
print("-------------------------")