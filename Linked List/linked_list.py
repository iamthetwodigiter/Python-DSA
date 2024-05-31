# Creates a Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Linked List Constructor
    def __init__(self, data):
        newnode = Node(data)
        self.head = newnode
        self.tail = newnode
        self.length = 1

    # Print the Linked List
    def print_list(self):
        temp = self.head
        print("Head  =>  ", end="")
        while temp is not None:
            print(temp.data, end="  =>  ")
            temp = temp.next
        print("None")

    # Append items to the Linked List
    def append(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
        self.length += 1
        return True  # Optional

    # Pop items from the Linked List
    def pop(self):
        if self.length == 0:  # if self.head is None:
            return None

        temp = self.head
        prev = self.head

        while temp.next:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    # Append the item at the beginning of the Linked List
    def prepend(self, data):
        newnode = Node(data)
        if self.length == 0:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head = newnode
        self.length += 1
        return True
    

linked_list = LinkedList(40)
linked_list.append(20)
linked_list.print_list()
x = linked_list.pop()
x = linked_list.pop()
x = linked_list.pop()
print(x)
