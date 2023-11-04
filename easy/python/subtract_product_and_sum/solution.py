"""
Given an integer number n, return the difference between the product of its
digits and the sum of its digits.
"""

from unittest import TestCase


class Solution:
    """Solves iteratively in constant space and logarithmic time."""

    @staticmethod
    def subtract_product_and_sum(number: int) -> int:
        """Returns difference of product and sum of integers."""
        product = 1
        sum_ = 0
        while number:
            product *= number % 10
            sum_ += number % 10
            number //= 10
        return product - sum_


class TestSubtractProductAndSum(TestCase):
    def test_minimum_input(self):
        expected = 0
        result = Solution.subtract_product_and_sum(1)
        self.assertEqual(expected, result)

    def test_typical_input_1(self):
        expected = 14
        result = Solution.subtract_product_and_sum(1234)
        self.assertEqual(expected, result)

    def test_typical_input_2(self):
        expected = -14
        result = Solution.subtract_product_and_sum(905)
        self.assertEqual(expected, result)

    def test_typical_input(self):
        expected = -3
        result = Solution.subtract_product_and_sum(1111)
        self.assertEqual(expected, result)
