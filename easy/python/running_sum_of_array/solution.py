"""
Given an array nums. We define a running sum of an array as runningSum[i] =
sum(nums[0]…nums[i]).

Return the running sum of nums.
"""

from typing import List, Iterator
from unittest import TestCase
from itertools import accumulate


class Solution:
    """Solves iteratively in linear time and constant space."""

    @staticmethod
    def running_sum(nums: List[int]) -> Iterator[int]:
        """
        Return the running sum of an array.
        :param nums: the array to sum.
        :return: an array of sums at each step.
        """
        assert 1 <= len(nums) <= 1000

        return accumulate(nums)


class TestRunningSum(TestCase):
    def test_zero_input(self):
        expected = [0]
        result = Solution.running_sum([0])
        self.assertListEqual(expected, list(result))

    def test_negative_input(self):
        expected = [-5, -9, -12, -14, -15]
        result = Solution.running_sum([-5, -4, -3, -2, -1])
        self.assertListEqual(expected, list(result))

    def test_typical_input(self):
        expected = [1, 3, 6, 10, 15]
        result = Solution.running_sum([1, 2, 3, 4, 5])
        self.assertListEqual(expected, list(result))
