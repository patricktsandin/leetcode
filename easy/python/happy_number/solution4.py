from math import log


class Solution:
    def __init__(self):
        self.intermediates = set()

    def is_happy(self, n: int) -> bool:
        """
        Return whether a number is happy using a recursive algorithm.
        :param n: Potential happy number
        :return: Whether it is happy
        """
        if n == 1:
            return True
        elif n in self.intermediates:
            return False
        else:
            self.intermediates.add(n)
            n = sum([
                (n // 10**p % 10)**2
                for p in range(int(log(n, 10)) + 1)
            ])
            return self.is_happy(n)
