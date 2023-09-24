# Implement a last-in-first-out (LIFO) stack using only two queues. The
# implemented stack should support all the functions of a normal stack (push,
# top, pop, and empty).

class MyStack:
    """Implements a stack using queues."""
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.insert(0, x)

    def pop(self) -> int:
        """Pops from stack by cycling queue."""
        for _ in range(len(self.queue) - 1):
            self.queue.insert(0, self.queue.pop())
        return self.queue.pop()

    def top(self) -> int:
        """Peeks stack by cycling queue."""
        for _ in range(len(self.queue) - 1):
            self.queue.insert(0, self.queue.pop())
        top = self.queue[-1]
        self.queue.insert(0, self.queue.pop())
        return top

    def empty(self) -> bool:
        return not self.queue
