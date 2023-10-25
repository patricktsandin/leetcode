"""
You are given positive integers n and m.
Define two integers, num1 and num2, as follows:
num1: The sum of all integers in the range [1, n] that are not divisible by m.
num2: The sum of all integers in the range [1, n] that are divisible by m.
Return the integer num1 - num2.
"""
from unittest import TestCase


class Solution:
    """Solves iteratively in constant time and space."""

    @staticmethod
    def range_sum(start: int, stop: int, /, *, step: int = 1) -> int:
        """
        Sums a sequence of integers with an optional step.
        :param start: Start of sequence, inclusive
        :param stop: End of sequence, exclusive
        :param step: Optional integer step between sequence elements
        :return: Sum of selected integers
        """
        assert start > 0 and stop > 0 and step > 0

        if start % step != 0:
            start += step - (start % step)

        if stop % step != 0:
            stop -= (stop % step) - step

        count = (stop - start) // step
        median = (stop + start - step) / 2

        return int(median*count)

    def difference_of_sums(self, upper_bound: int, divisor: int) -> int:
        """Returns the difference of the sums of the integers in a range
        which are divisible and not divisible by a given divisor.
        :param upper_bound: the inclusive upper bound of a range starting at 1
        :param divisor: the integer by which to divide numbers in the range
        """
        assert 1 <= upper_bound <= 1000
        assert 1 <= divisor <= 1000

        divisible_sum = self.range_sum(divisor, upper_bound + 1, step=divisor)
        indivisible_sum = self.range_sum(1, upper_bound + 1) - divisible_sum

        return indivisible_sum - divisible_sum


class TestSequenceSum(TestCase):
    def test_bad_stop(self):
        self.assertRaises(AssertionError, Solution().range_sum, -9, 1)

    def test_minimums(self):
        expected = 1
        result = Solution.range_sum(1, 2)
        self.assertEqual(expected, result)

    def test_contiguous_range(self):
        expected = 54
        result = Solution.range_sum(2, 11)
        self.assertEqual(expected, result)

    def test_evens_with_even_boundaries_from_2(self):
        expected = 20
        result = Solution.range_sum(2, 10, step=2)
        self.assertEqual(expected, result)

    def test_evens_with_odd_boundaries(self):
        expected = 30
        result = Solution.range_sum(1, 11, step=2)
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

    def test_typical_case(self):
        expected = 357129
        result = Solution().difference_of_sums(upper_bound=926, divisor=12)
        self.assertEqual(expected, result)
