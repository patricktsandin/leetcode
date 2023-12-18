"""
You are given a positive integer num consisting of exactly four digits. Split
num into two new integers new1 and new2 by using the digits found in num.
Leading zeros are allowed in new1 and new2, and all the digits found in num
must be used.
For example, given num = 2932, you have the following digits: two 2's,
one 9 and one 3. Some of the possible pairs [new1, new2] are [22, 93], [23,
92], [223, 9] and [2, 329].
Return the minimum possible sum of new1 and new2.
"""

from unittest import TestCase


class Solution:
    """Solves iteratively in linear space and O(n log n) time."""

    @staticmethod
    def minimum_sum(number: int) -> int:
        """Calculate the minimum sum of two integers derived from the
        digits of an input integer."""
        digits = sorted(list(str(number)))
        operand_1 = int(''.join(digits[::2]))
        operand_2 = int(''.join(digits[1::2]))
        return operand_1 + operand_2


class TestMinimumSum(TestCase):
    def test_minimum_input(self):
        expected = 1
        result = Solution.minimum_sum(1000)
        self.assertEqual(expected, result)

    def test_maximum_input(self):
        expected = 198
        result = Solution.minimum_sum(9999)
        self.assertEqual(expected, result)

    def test_typical_input_1(self):
        expected = 37
        result = Solution.minimum_sum(1234)
        self.assertEqual(expected, result)

    def test_typical_input_2(self):
        expected = 66
        result = Solution.minimum_sum(975)
        self.assertEqual(expected, result)
