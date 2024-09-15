from _collections_abc import Iterable


class Node:
    def __init__(self, data, next) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_begin(self, val):
        node = Node(val, self.head)
        self.head = node

    def insert_at_end(self, val):
        if self.head is None:
            self.head = Node(val, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(val, None)

    def insert_all(self, val: Iterable[str]) -> None:
        for elements in val:
            self.insert_at_end(elements)

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstring = ""

        while itr:
            llstring += str(itr.data) + " -> "
            itr = itr.next

        print(llstring + "None")

    def length(self):
        ll_size = 0

        itr = self.head
        while itr:
            ll_size += 1
            itr = itr.next

        return ll_size

    def remove_at(self, index):
        if index < 0 or index >= self.length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        itr = self.head
        count = 0

        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, value):
        if index < 0 or index >= self.length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_begin(value)

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(value, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node

        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next
            if itr is None:
                print(f"The linked list did not contain the occurance of {data_after}")

    def remove_by_value(self, value):
        # Remove first node that contains data

        if self.head is None:
            print("Empty Linked list")

        if self.head.data == value:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == value:
                itr.next = itr.next.next
                return
            itr = itr.next


if __name__ == "__main__":
    random_stuff = ["banana", "mango", "icecream", "silviakaka"]

    my_list = LinkedList()

    my_list.insert_all(random_stuff)

    # my_list.insert_at_begin(2)
    # my_list.insert_at_begin(5)
    # my_list.print()

    # my_list.insert_at_end(10)
    my_list.insert_at(2, "cookies")
    my_list.insert_at(3, "cream")
    my_list.insert_after_value("cream", "hello")
    my_list.insert_after_value("cream1", "hello")
    my_list.remove_by_value("cream")
    my_list.print()
    # my_list.remove_at(2)
    # my_list.remove_at(20)
    # my_list.print()
