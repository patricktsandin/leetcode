"""
Given two arrays of integers nums and index. Your task is to create target
array under the following rules:
- Initially target array is empty.
- From left to right read nums[i] and index[i], insert at index index[i] the
value nums[i] in target array.
- Repeat the previous step until there are no elements to read in nums and index.
Return the target array.
It is guaranteed that the insertion operations will be valid.

Constraints:
1 <= nums.length, index.length <= 100
nums.length == index.length
0 <= nums[i] <= 100
0 <= index[i] <= i
"""


from unittest import TestCase
from typing import List


class Solution:
    """Solves iteratively in linear time and space."""

    @staticmethod
    def create_target_array(nums: List[int], indexes: List[int]) -> List[int]:
        """
        Given lists of integers and indexes, return a list with those integers
        at those indexes
        :param nums: list of integers to place
        :param indexes: list of indexes in which to place them
        :return: resultant list
        """
        assert len(nums) == len(indexes) and len(nums) > 0

        result = []
        for index, num in zip(indexes, nums):
            result.insert(index, num)
        return result


# noinspection DuplicatedCode
class TestCreateTargetArray(TestCase):
    def test_minimum(self):
        expected = [0]
        result = Solution.create_target_array([0], [0])
        self.assertListEqual(expected, result)

    def test_typical_1(self):
        expected = [0, 4, 1, 3, 2]
        result = Solution.create_target_array([0, 1, 2, 3, 4], [0, 1, 2, 2, 1])
        self.assertListEqual(expected, result)

    def test_typical_2(self):
        expected = [0, 1, 2, 3, 4]
        result = Solution.create_target_array([1, 2, 3, 4, 0], [0, 1, 2, 3, 0])
        self.assertListEqual(expected, result)
