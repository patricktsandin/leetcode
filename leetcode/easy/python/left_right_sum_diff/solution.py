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
from typing import List


class Solution:
    """Solves iteratively in exponential time and linear space."""

    @staticmethod
    def left_right_difference(nums: List[int]) -> List[int]:
        """Find the absolute values of the differences between the summed halves
        of a list divided by a sliding pivot point."""
        assert len(nums) > 0

        return [
            abs(sum(nums[:i]) - sum(nums[i + 1:])) for i in range(len(nums))
        ]


class TestLeftRightDifference(TestCase):
    def test_minimum(self):
        expected = [0]
        result = Solution.left_right_difference([1])
        self.assertListEqual(expected, result)

    def test_typical_1(self):
        expected = [15, 1, 11, 22]
        result = Solution.left_right_difference([10, 4, 8, 3])
        self.assertListEqual(expected, result)
