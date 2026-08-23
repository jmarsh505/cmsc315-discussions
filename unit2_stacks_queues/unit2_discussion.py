"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque
import queue


class Stack:
    def __init__(self):
        # A list stores the values in the stack.
        self.items = []

    def push(self, value):
        # New values go on top, supporting last-in-first-out (LIFO) behavior.
        self.items.append(value)

    def pop(self):
        # Prevent an attempt to pop from an empty stack.
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")

        return self.items.pop()
    
    def peek(self):
        # Prevent an attempt to peek at an empty stack.
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack.")

        return self.items[-1]

    def is_empty(self):
        # Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # A deque for removal from the front of the que.
        self.items = deque()

    def enqueue(self, value):
        # New values enter at the back, supporting first-in-first-out (FIFO) behavior.
        self.items.append(value)

    def dequeue(self):
        # Prevent an attempt to remove an item from an empty queue.
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")
        
        return self.items.popleft()

    def front(self):
        # Front returns the next value to leave without removing it.

        # Prevent an attempt to view the front of an empty queue.
        if self.is_empty():
            raise IndexError("Cannot view the front of an empty queue.")

        return self.items[0]
    
    def is_empty(self):
        # Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # STACK DEMO
    # ===============================

    print("\n=== STACK DEMO ===")

    stack = Stack()
    stack_values = ["Book", "Laptop", "Phone", "Tablet"]

    print("Adding four values to the stack:")
    for value in stack_values:
        stack.push(value)
        print(f"  Pushed: {value}")

    print(f"\nThe value on top of the stack is: {stack.peek()}")

    print("\nRemoving all values from the stack demonstrates LIFO behavior:")
    while not stack.is_empty():
        print(f"  Popped: {stack.pop()}")

    print("\nIs the stack empty? ", stack.is_empty())

    print("\nAttempting to pop from an empty stack:")
    try:
        stack.pop()
    except IndexError as e:
        print(f"  Caught an error: {e}")


    print("\nAttempting to peek at an empty stack:")
    try:
        stack.peek()
    except IndexError as e:
        print(f"  Caught an error: {e}")


    print("\nTesting a single-item stack:")
    single_item_stack = Stack()
    single_item_stack.push("SingleItem")
    print(f"  Popped: {single_item_stack.pop()}")
    print("Is the single-item stack empty? ", single_item_stack.is_empty())

# ===============================
# QUEUE DEMO
# ===============================

    print("\n=== QUEUE DEMO ===")

    queue = Queue()
    queue_values = ["First", "Second", "Third", "Fourth"]

    print("Adding four values to the queue:")
    for value in queue_values:
        queue.enqueue(value)
        print(f"  Enqueued: {value}")

    print(f"\nThe value at the front of the queue is: {queue.front()}")

    print("\nRemoving values demonstrates FIFO behavior:")
    while not queue.is_empty():
        print(f"  Dequeued: {queue.dequeue()}")

    print("\nIs the queue empty? ", queue.is_empty())

    print("\nAttempting to dequeue from an empty queue:")
    try:
        queue.dequeue()
    except IndexError as e:
        print(f"  Caught an error: {e}")

    print("\nAttempting to view the front of an empty queue:")
    try:
        queue.front()
    except IndexError as e:
        print(f"  Caught an error: {e}")


    print("\nTesting a single-item queue:")
    single_item_queue = Queue()
    single_item_queue.enqueue("SingleItem")
    print(f"  Dequeued: {single_item_queue.dequeue()}")
    print("Is the single-item queue empty? ", single_item_queue.is_empty())


if __name__ == "__main__":
    main()
