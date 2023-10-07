# Given a zero-based permutation nums (0-indexed), build an array ans of the
# same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and
# return it.

from typing import List


class Solution:
    @staticmethod
    def build_array(nums: List[int]) -> List[int]:
        """Return array where elements are moved to indexes equal
        to themselves."""
        length = len(nums)
        for index, num in enumerate(nums):
            answer = nums[num] % length
            nums[index] += answer * length
        for index in range(length):
            nums[index] //= length
        return nums
