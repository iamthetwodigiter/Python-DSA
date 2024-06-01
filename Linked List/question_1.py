"""
Instructions:
Write a method to find and return the middle node in the Linked List WITHOUT using the length attribute.
"""
from linked_list import LinkedList

ll = LinkedList()

def middle(ll):
    slow = ll.head
    fast = ll.head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow

ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
ll.append(60)
ll.print_list()
middle_node = middle(ll)
print(middle_node.data)