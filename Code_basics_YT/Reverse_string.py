from collections import deque  # Since you're using deque, import it first.
from _collections_abc import Iterable


class Stack:
    def __init__(self) -> None:
        self.container = deque()

    def push(self, val) -> None:
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def push_all(self, val: Iterable[str]) -> None:
        for element in val:
            self.container.append(element)

    def reverse_string(self) -> str:
        reversed_str = ""

        while not self.is_empty():  # Loop while the stack is not empty
            reversed_str += self.pop()  # Pop from the stack and append to reversed_str
        return reversed_str


my_stack = Stack()
my_stack.push_all("We will conquer covid-19”")
my_stack.size()
my_stack.reverse_string()
