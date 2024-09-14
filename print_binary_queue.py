"""
Write a program to print binary numbers from 1 to 10 using Queue.
Use Queue class implemented in main tutorial.
Binary sequence should look like,
1
10
11
100
101
110
111
1000
1001
1010

"""

from collections import deque


class Queue:
    def __init__(self) -> None:
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[-1]


def print_binary(number):
    empty_queue = Queue()

    empty_queue.enqueue("1")

    for n in range(number):
        front = empty_queue.front()
        print("Printing the binary number: ", front)

        empty_queue.enqueue(front + "0")
        empty_queue.enqueue(front + "1")

        empty_queue.dequeue()


if __name__ == "__main__":
    print_binary(10)
