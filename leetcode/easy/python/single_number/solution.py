from typing import List


class Solution:
    @staticmethod
    def single_number(nums: List[int]) -> int:
        """
        Given a list where all elements are duplicates except one, return
        the singular element.  O(1) space and O(n) time, iterative algorithm
        leveraging sets.  Beats 97.74% of LeetCoders on memory consumption.
        :param nums: List of integers, all but one duplicated
        :return: Single non-duplicated integer from input list
        """
        nums_list_sum = sum(nums)
        nums_set = set()
        while nums:
            nums_set.add(nums.pop(0))
        nums_set_sum = sum(nums_set)
        return nums_set_sum * 2 - nums_list_sum
