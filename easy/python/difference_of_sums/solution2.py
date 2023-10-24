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
    def sequence_sum(stop: int, step: int = 1) -> int:
        """
        Sums a sequence of integers with an optional step.
        :param stop: End of sequence, inclusive
        :param step: Optional integer step between sequence elements
        :return: Sum of selected integers
        """
        assert stop > 0 and step > 0
        return sum(range(0, stop+1, step))

    def difference_of_sums(self, upper_bound: int, divisor: int) -> int:
        """Returns the difference of the sums of the integers in a range
        which are divisible and not divisible by a given divisor.
        :param upper_bound: the inclusive upper bound of a range starting at 1
        :param divisor: the integer by which to divide numbers in the range
        """
        assert 1 <= upper_bound <= 1000
        assert 1 <= divisor <= 1000

        divisible_sum = self.sequence_sum(upper_bound, divisor)
        indivisible_sum = self.sequence_sum(upper_bound) - divisible_sum

        return indivisible_sum - divisible_sum


class TestSequenceSum(TestCase):
    def test_bad_stop(self):
        self.assertRaises(AssertionError, Solution().sequence_sum, -9, 1)

    def test_minimums(self):
        expected = 1
        result = Solution.sequence_sum(1)
        self.assertEqual(expected, result)


class TestSumsDifference(TestCase):
    def test_minimum_upper_bound_and_divisor(self):
        expected = -1
        result = Solution().difference_of_sums(upper_bound=1, divisor=1)
        self.assertEqual(expected, result)

    def test_maximum_upper_bound_and_divisor(self):
        expected = 498500
        result = Solution().difference_of_sums(upper_bound=1000, divisor=1000)
        self.assertEqual(expected, result)

    def test_maximum_upper_bound_and_minimum_divisor(self):
        expected = -500500
        result = Solution().difference_of_sums(upper_bound=1000, divisor=1)
        self.assertEqual(expected, result)

    def test_minimum_upper_bound_and_maximum_divisor(self):
        expected = 1
        result = Solution().difference_of_sums(upper_bound=1, divisor=1000)
        self.assertEqual(expected, result)
