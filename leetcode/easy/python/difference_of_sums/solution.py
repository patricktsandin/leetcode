"""
You are given positive integers n and m.
Define two integers, num1 and num2, as follows:
num1: The sum of all integers in the range [1, n] that are not divisible by m.
num2: The sum of all integers in the range [1, n] that are divisible by m.
Return the integer num1 - num2.
"""
from unittest import TestCase


class Solution:
    """Solves iteratively in linear time and constant space."""

    @staticmethod
    def difference_of_sums(upper_bound: int, divisor: int) -> int:
        """Returns the difference of the sums of the integers in a range
        which are divisible and not divisible by a given divisor.
        :param upper_bound: the inclusive upper bound of a range starting at 1
        :param divisor: the integer by which to divide numbers in the range
        """
        assert 1 <= upper_bound <= 1000
        assert 1 <= divisor <= 1000

        return (
            sum(n for n in range(upper_bound+1) if n % divisor)
            - sum(n for n in range(upper_bound+1) if not n % divisor)
        )


class TestSumsDifference(TestCase):
    """Check edge cases."""

    def test_minimum_upper_bound_and_divisor(self):
        result = Solution.difference_of_sums(upper_bound=1, divisor=1)
        expected = -1
        self.assertEqual(expected, result)

    def test_maximum_upper_bound_and_divisor(self):
        result = Solution.difference_of_sums(upper_bound=1000, divisor=1000)
        expected = 498500
        self.assertEqual(expected, result)

    def test_maximum_upper_bound_and_minimum_divisor(self):
        result = Solution.difference_of_sums(upper_bound=1000, divisor=1)
        expected = -500500
        self.assertEqual(expected, result)

    def test_minimum_upper_bound_and_maximum_divisor(self):
        result = Solution.difference_of_sums(upper_bound=1, divisor=1000)
        expected = 1
        self.assertEqual(expected, result)
