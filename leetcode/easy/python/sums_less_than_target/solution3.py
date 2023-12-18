"""
Given a 0-indexed integer array nums of length n and an integer target,
return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j]
< target.
"""

from unittest import TestCase
from typing import List


class Solution:
    """Solves iteratively in constant space and O(n log n) time."""

    @staticmethod
    def count_pairs(numbers: List[int], target: int) -> int:
        """
        Returns the number of pairs from an input list that sum to
        less than target.
        """
        assert 1 <= len(numbers) <= 50
        assert -50 <= target <= 50

        pair_count = 0
        low_pointer = 0
        high_pointer = len(numbers) - 1
        numbers.sort()

        while high_pointer > low_pointer:
            if numbers[high_pointer] + numbers[low_pointer] >= target:
                high_pointer -= 1
            else:
                pair_count += high_pointer - low_pointer
                low_pointer += 1
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

    def test_typical_input_1(self):
        expected = 7
        result = Solution.count_pairs([48, 1, 2, 8, 6, 50], 50)
        self.assertEqual(expected, result)

    def test_typical_input_2(self):
        expected = 6
        result = Solution.count_pairs([92, 1, 18, 23, 30, 41], 50)
        self.assertEqual(expected, result)

    def test_odd_length_input(self):
        expected = 12
        result = Solution.count_pairs([9, 8, 7, 6, 5, 4, 3, 2, 1], 9)
        self.assertEqual(expected, result)

    def test_even_length_input(self):
        expected = 6
        result = Solution.count_pairs([9, 8, 7, 6, 5, 4, 3, 2], 9)
        self.assertEqual(expected, result)

    def test_zeros(self):
        expected = 0
        result = Solution.count_pairs([0, 0, 0, 0, 0, 0], 0)
        self.assertEqual(expected, result)
