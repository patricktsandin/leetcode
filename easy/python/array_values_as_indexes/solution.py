# Given a zero-based permutation nums (0-indexed), build an array ans of the
# same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and
# return it.

from typing import List


class Solution:
    @staticmethod
    def build_array(nums: List[int]) -> List[int]:
        """Return array where elements are moved to indexes equal
        to themselves."""
        ans = [0]*len(nums)
        for i, num in enumerate(nums):
            ans[i] = nums[num]
        return ans
