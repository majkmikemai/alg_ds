# Suppose this is your linked list structure
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Create a linked list: 1 -> 2 -> 3
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

# node1 is the head of the list
node1
