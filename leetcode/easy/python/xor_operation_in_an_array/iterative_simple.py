"""Solves 1486: 'XOR Operation in an Array'.

You are given an integer n and an integer start.
Define an array nums where nums[i] = start + 2 * i (0-indexed) and n ==
nums.length.
Return the bitwise XOR of all elements of nums.

Constraints:
1 <= n <= 1000
0 <= start <= 1000
n == nums.length
"""


from typing import Self
from unittest import TestCase


class Solution:
    """Solves iteratively in linear time and constant space."""

    @staticmethod
    def xor_operation(n: int, start: int) -> int:
        """XORs a sequence of integers.

        Sequence follows formula:
        integer = start + 2 * i for i = start,...,n-1.
        """
        assert n > 0
        assert start >= 0

        accumulator = 0
        for _ in range(n):
            accumulator ^= start
            start += 2

        return accumulator


# noinspection DuplicatedCode
class TestXOROperation(TestCase):
    """Test Solution.xor_operation()."""

    def test_minimums(self: Self) -> None:
        """Test minimum inputs."""
        expected = 0
        result = Solution().xor_operation(1, 0)
        self.assertEqual(expected, result)

    def test_typical_1(self: Self) -> None:
        """Test typical input."""
        expected = 8
        result = Solution().xor_operation(5, 0)
        self.assertEqual(expected, result)

    def test_typical_2(self: Self) -> None:
        """Test typical input."""
        expected = 8
        result = Solution().xor_operation(4, 3)
        self.assertEqual(expected, result)
