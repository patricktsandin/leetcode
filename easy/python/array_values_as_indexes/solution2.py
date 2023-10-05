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
        first_element = nums[0]
        index = 0
        while True:
            last_overwritten_element = nums[index]
            if last_overwritten_element < 0:
                if index == length - 1:
                    index = 0
                    continue
                else:
                    index += 1
                    continue
            if index == 0:
                last_overwritten_element = first_element

            nums[index] = -nums[last_overwritten_element]
            index = abs(last_overwritten_element)
        return nums
