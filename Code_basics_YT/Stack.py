from collections import deque  # Since you're using deque, import it first.


class Stack:
    def __init__(self) -> None:
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


# Create an instance of the Stack class
my_stack = Stack()


my_stack.push(10)
my_stack.push(20)
my_stack.push(30)


my_stack.pop()
my_stack.peek()
my_stack.is_empty()
my_stack.size()
