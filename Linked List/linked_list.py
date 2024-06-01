# Creates a Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Linked List Constructor
    def __init__(self):
        # Removed the creation of newnode in the constructor itself
        self.head = None
        self.tail = None
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
    
    # Removes the first element from the Linked List
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    # Returns the node at the particular index
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    # Set the data of node equal to the data, at that particular index [We are setting or replacing the value and not inserting another node]
    def set_value(self, index, data):
        temp = self.get(index)
        if temp:
            temp.data = data
            return True
        return False
    
    # Insert data at a particular index
    def insert(self, index, data):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(data)
        if index == self.length:
            return self.append(data)
        newnode = Node(data)
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        newnode.next = temp.next
        temp.next = newnode
        self.length += 1
        return True
    
    # Removes an item at a particular index
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    # Reverse the Linked List
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        
def main():
    ll = LinkedList()
    options = ['Append', 'Prepend', 'Insert', 'Pop', 'Pop First', 'Remove', 'Get', 'Set', 'Reverse', 'Print']
    for i,items in enumerate(options):
        print(f'{i+1}. {items}')
    while True:   
        choice = input("Enter your choice: ")

        if choice == "1":
            data = input("Enter data: ")
            ll.append(data)
            ll.print_list()
        elif choice == "2":
            data = input("Enter data: ")
            ll.prepend(data)
            ll.print_list()
        elif choice == "3":
            index = int(input("Enter index: "))
            data = input("Enter data: ")
            ll.insert(index, data)
            ll.print_list()
        elif choice == "4":
            popped = ll.pop()
            print(f"Popped: {popped.data}\n")
            ll.print_list()
        elif choice == "5":
            popped = ll.pop_first()
            print(f"Popped: {popped.data}\n")
            ll.print_list()
        elif choice == "6":
            index = int(input("Enter index: "))
            removed = ll.remove(index)
            print(f"Removed: {removed.data}\n")
            ll.print_list()
        elif choice == "7":
            index = int(input("Enter index: "))
            data = ll.get(index).data
            print(f"Data at index {index}: {data}\n")
        elif choice == "8":
            index = int(input("Enter index: "))
            data = input("Enter data: ")
            ll.set_value(index, data)
            ll.print_list()
        elif choice == "9":
            ll.reverse()
            ll.print_list()
        elif choice == "10":
            ll.print_list()
        else:
            exit()

if __name__ == '__main__':
    main()