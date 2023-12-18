"""
Given a 0-indexed integer array nums, find a 0-indexed integer array answer
where:
answer.length == nums.length.
answer[i] = |leftSum[i] - rightSum[i]|.
Where:
leftSum[i] is the sum of elements to the left of the index i in the array
nums. If there is no such element, leftSum[i] = 0.
rightSum[i] is the sum of elements to the right of the index i in the array
nums. If there is no such element, rightSum[i] = 0.
Return the array answer.

Constraints:
1 <= nums.length <= 1000
1 <= nums[i] <= 105
"""


from unittest import TestCase
from typing import List, Iterator
from itertools import islice


class Solution:
    """Solves iteratively in linear time and constant space."""

    @staticmethod
    def left_right_difference(nums: List[int]) -> Iterator[int]:
        """Find the absolute values of the differences between the summed halves
        of a list divided by a sliding pivot point."""
        assert len(nums) > 0

        first_half_sum = 0
        second_half_sum = sum(islice(nums, 1, None))
        yield abs(first_half_sum - second_half_sum)
        for i in range(len(nums) - 1):
            first_half_sum += nums[i]
            second_half_sum -= nums[i+1]
            yield abs(first_half_sum - second_half_sum)


class TestLeftRightDifference(TestCase):
    def test_minimum(self):
        expected = [0]
        result = Solution.left_right_difference([1])
        self.assertListEqual(expected, list(result))

    def test_typical_1(self):
        expected = [15, 1, 11, 22]
        result = Solution.left_right_difference([10, 4, 8, 3])
        self.assertListEqual(expected, list(result))
