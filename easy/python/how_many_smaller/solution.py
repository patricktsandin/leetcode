"""
Given the array nums, for each nums[i] find out how many numbers in the array
are smaller than it. That is, for each nums[i] you have to count the number
of valid j's such that j != i and nums[j] < nums[i].
Return the answer in an array.
"""

from unittest import TestCase
from typing import List
from itertools import pairwise


class Solution:
    """Solves iteratively in linear space and O(n log n) time."""

    @staticmethod
    def smallerNumbersThanCurrent(numbers: List[int]) -> List[int]:
        """
        Given a list of numbers, check how many of their siblings are
        smaller.
        :param numbers: list to check
        :return: list of smaller sibling counts
        """
        smaller_counts = {0: 0}
        sorted_pairs = enumerate(pairwise(sorted([0] + numbers)))
        for i, (previous, current) in sorted_pairs:
            if current > previous:
                smaller_counts[current] = i
        return [smaller_counts[n] for n in numbers]


class TestSmallerNumbersThanCurrent(TestCase):
    def test_minimum_input(self):
        expected = [0, 0]
        result = Solution.smallerNumbersThanCurrent([0, 0])
        self.assertListEqual(expected, result)

    def test_minimum_length(self):
        expected = [1, 0]
        result = Solution.smallerNumbersThanCurrent([9, 0])
        self.assertListEqual(expected, result)

    def test_minimum_values(self):
        expected = [0, 0, 0, 0, 0, 0]
        result = Solution.smallerNumbersThanCurrent([0, 0, 0, 0, 0, 0])
        self.assertListEqual(expected, result)

    def test_typical_input_1(self):
        expected = [0, 4, 2, 3, 5, 6, 0]
        result = Solution.smallerNumbersThanCurrent([2, 9, 6, 8, 10, 55, 2])
        self.assertListEqual(expected, result)

    def test_typical_input_2(self):
        expected = [5, 1, 3, 4, 0, 2, 6]
        result = Solution.smallerNumbersThanCurrent([9, 2, 6, 8, 1, 5, 12])
        self.assertListEqual(expected, result)