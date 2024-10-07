"""
Place Order: This thread will be placing an order and inserting that into a queue.
This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)

Serve Order: This thread will server the order.
All you need to do is pop the order out of the queue and print it.
This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.

"""

import time
import threading
from collections import deque
from collections.abc import Iterable


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

    def place_order(self, orders: Iterable[str]) -> None:
        for order in orders:
            print(f"Placing order: {order}")
            self.enqueue(order)
            time.sleep(0.5)

    def serve_order(self):
        while True:
            if not self.is_empty():
                order = self.dequeue()
                print(f"Serving order: {order}")
            else:
                print("No orders to serve, waiting...")
                break
            time.sleep(2)  # Wait 2 seconds before serving the next order


# Orders to be placed


orders = ["pizza", "samosa", "pasta", "biryani", "burger"]

food_system = Queue()

timer = time.time()

ordering_thread = threading.Thread(target=food_system.place_order, args=(orders,))
serving_thread = threading.Thread(target=food_system.serve_order)


ordering_thread.start()

time.sleep(1)
serving_thread.start()

ordering_thread.join()
serving_thread.join()

print("the orders and service has been finished")
