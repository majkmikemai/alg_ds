from collections import deque  # Since you're using deque, import it first.
from _collections_abc import Iterable

"""
Write a function in python that checks if parenthesis in the string are balanced or not. Possible parenthesis are “{}”, “()” or “[]”. 
"""


class Stack:
    def __init__(self) -> None:
        self.container = deque()
        self.opening_parenthesis = ["{", "(", "["]
        self.closing_parentesis = ["}", ")", "]"]

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

    def is_balanced(self, val) -> bool:
        for element in val:
            if element in self.opening_parenthesis:
                self.container.append(element)
            elif element in self.closing_parentesis:
                index = self.closing_parentesis.index(element)

                if self.is_empty() or self.peek() != self.opening_parenthesis[index]:
                    return False
                self.container.pop()
        return self.is_empty()


my_stack = Stack()
my_stack.is_balanced("({a+b})")
my_stack.is_balanced("))((a+b}{")  # --> False
my_stack.is_balanced("((a+b))")  # --> True
my_stack.is_balanced("))")  # --> False
my_stack.is_balanced("[a+b]*(x+2y)*{gg+kk}")  # --> True
