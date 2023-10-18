"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the
squares of its digits.
Repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""

from math import log


class Solution:
    """Solves using iterative algorithm."""

    @staticmethod
    def is_happy(n: int) -> bool:
        """
        Return whether a number is happy
        :param n: Potential happy number
        :return: Whether it is happy
        """
        while n != 1:
            # noinspection IncorrectFormatting
            n = sum((n//10**p % 10)**2 for p in range(int(log(n, 10)) + 1))
            if n == 4:
                return False

        return True
