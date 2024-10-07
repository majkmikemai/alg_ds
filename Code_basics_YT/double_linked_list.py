class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            itr = self.head

            while itr.next:
                itr = itr.next

            itr.next = node
            node.prev = itr
            itr.next = node
            node.next = None

    def prepend(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            old_head = self.head
            old_head.prev = node
            node.next = old_head
            self.head = node
        self.head.prev = None

    def RemoveFront(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def RemoveEnd(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.prev.next = None

    def print_all(self):
        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next


if __name__ == "__main__":
    dll = DoubleLinkedList()
    dll.prepend(0)
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.RemoveEnd()
    dll.print_all()
