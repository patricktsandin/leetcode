from math import log


class Solution:
    @staticmethod
    def is_happy(n: int) -> bool:
        """
        Return whether a number is happy
        :param n: Potential happy number
        :return: Whether it is happy
        """
        all_n = set()
        while n is not 1:
            n = sum([(n // 10**p % 10)**2 for p in range(int(log(n, 10)) + 1)])
            if n in all_n:
                break
            else:
                all_n.add(n)
        return n is 1
