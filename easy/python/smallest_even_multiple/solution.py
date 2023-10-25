"""
Given a positive integer n, return the smallest positive integer that is a
multiple of both 2 and n.
"""

from unittest import TestCase


class Solution:
    """Solves in constant time and constant space."""

    @staticmethod
    def smallest_even_multiple(n: int) -> int:
        """Returns the least common multiple of 2 and n."""
        assert 1 <= n <= 150

        return n if n % 2 == 0 else 2*n


class TestSmallestEvenMultiple(TestCase):
    def test_even_number(self):
        expected = 2
        result = Solution.smallest_even_multiple(2)
        self.assertEqual(expected, result)

    def test_odd_number(self):
        expected = 2
        result = Solution.smallest_even_multiple(1)
        self.assertEqual(expected, result)

    def test_large_number(self):
        expected = 298
        result = Solution.smallest_even_multiple(149)
        self.assertEqual(expected, result)
