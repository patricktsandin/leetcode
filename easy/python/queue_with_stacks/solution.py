# Implement a first in first out (FIFO) queue using only two stacks. The
# implemented queue should support all the functions of a normal queue (push,
# peek, pop, and empty).


class MyQueue:
    """A queue implemented using only stacks."""

    def __init__(self):
        self.push_stack = list()
        self.pop_stack = list()

    def push(self, x: int) -> None:
        while self.pop_stack:
            self.push_stack.append(self.pop_stack.pop())
        self.push_stack.append(x)
        while self.push_stack:
            self.pop_stack.append(self.push_stack.pop())

    def pop(self) -> int:
        return self.pop_stack.pop()

    def peek(self) -> int:
        return self.pop_stack[-1]

    def empty(self) -> bool:
        return not self.pop_stack
