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

    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")

    # 🔁 Reverse using STACK (your method)
    def reverse(self):
        temp = self.head
        stack = []

        # store values
        while temp is not None:
            stack.append(temp.value)
            temp = temp.next

        # put values back in reverse order
        temp = self.head   # ✅ FIXED
        while temp is not None:
            temp.value = stack.pop()
            temp = temp.next


# create list
ll = Linkedlist()
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

# display original
print("Original List:")
ll.display()

# reverse
ll.reverse()

# display reversed
print("Reversed List:")
ll.display()