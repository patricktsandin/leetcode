"""
Given two integers num1 and num2, return the sum of the two integers.
"""

from unittest import TestCase


class Solution:
    """Solves in constant time and space"""

    @staticmethod
    def sum(num1: int, num2: int) -> int:
        """
        Adds two integers
        :param num1: first operand
        :param num2: second operand
        :return: sum
        """
        return num1 + num2


class AdditionTest(TestCase):
    def test_adding_nothing_to_nothing(self):
        expected = 0
        result = Solution.sum(0, 0)
        self.assertEqual(expected, result)

    def test_adding_something_to_nothing(self):
        expected = 1
        result = Solution.sum(1, 0)
        self.assertEqual(expected, result)

    def test_adding_nothing_to_something(self):
        expected = 1
        result = Solution.sum(0, 1)
        self.assertEqual(expected, result)

    def test_adding_random_integers(self):
        expected = 533684
        result = Solution.sum(239842, 293842)
        self.assertEqual(expected, result)
