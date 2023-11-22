"""
You are given an integer n and an integer start.
Define an array nums where nums[i] = start + 2 * i (0-indexed) and n ==
nums.length.
Return the bitwise XOR of all elements of nums.

Constraints:
1 <= n <= 1000
0 <= start <= 1000
n == nums.length
"""


from unittest import TestCase


class Solution:
    """Solves recursively in linear time and space."""

    def xor_operation(self, n: int, start: int) -> int:
        """XORs a sequence of integers following the formula
        integer = start + 2 * i for i = start,...,n-1"""
        assert start >= 0

        if n < 1:
            return 0

        return (start + 2 * (n - 1)) ^ self.xor_operation(n - 1, start)


class TestXOROperation(TestCase):
    def test_minimums(self):
        expected = 0
        result = Solution().xor_operation(1, 0)
        self.assertEqual(expected, result)

    def test_typical_1(self):
        expected = 8
        result = Solution().xor_operation(5, 0)
        self.assertEqual(expected, result)

    def test_typical_2(self):
        expected = 8
        result = Solution().xor_operation(4, 3)
        self.assertEqual(expected, result)
