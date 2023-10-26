"""
Given a 0-indexed integer array nums of length n and an integer target,
return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j]
< target.
"""

from unittest import TestCase
from typing import List


class Solution:
    """Solves iteratively in linear space and exponential time."""

    @staticmethod
    def count_pairs(numbers: List[int], target: int) -> int:
        """
        Returns the number of ordered pairs from an input list that sum to
        less than target.
        """
        assert 1 <= len(numbers) <= 50
        assert -50 <= target <= 50

        pair_count = 0
        for i, number1 in enumerate(numbers):
            for _, number2 in enumerate(numbers[i + 1:]):
                if number1 + number2 < target:
                    pair_count += 1
        return pair_count


class TestCountPairs(TestCase):
    def test_single_item_input(self):
        expected = 0
        result = Solution.count_pairs([-50], 0)
        self.assertEqual(expected, result)

    def test_minimum_input(self):
        expected = 1
        result = Solution.count_pairs([-50, -50], -50)
        self.assertEqual(expected, result)

    def test_typical_input(self):
        expected = 7
        result = Solution.count_pairs([48, 1, 2, 8, 6, 50], 50)
        self.assertEqual(expected, result)

    def test_zeros(self):
        expected = 0
        result = Solution.count_pairs([0, 0, 0, 0, 0, 0], 0)
        self.assertEqual(expected, result)
