"""Functional Python Programming 3e

Chapter 1, Example Set 1

Convert the following to functional form:
def sum_numeric(limit: int) -> int:
    '''Sum a range of integers.'''
    s = 0
    for n in range(1, limit):
        if n % 3 == 0 or n % 5 == 0:
            s += n
    return s
"""

from unittest import TestCase


def sum_numeric(limit: int) -> int:
    """Sum a range of integers divisible by 3 or 5 between 0 and the limit."""
    return sum(n for n in range(limit) if n % 3 == 0 or n % 5 == 0)


class TestSumNumeric(TestCase):
    def test_sum_numeric(self) -> None:
        expected = 23
        result = sum_numeric(10)
        self.assertEqual(expected, result)
