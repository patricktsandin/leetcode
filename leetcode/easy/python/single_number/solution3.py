from typing import List
from operator import xor
from functools import reduce


class Solution:
    @staticmethod
    def single_number(nums: List[int]) -> int:
        """
        Given a list where all elements are duplicates except one, return
        the singular element.  O(1) space and O(n) time, iterative algorithm.
        Beats 79.34% of LeetCoders on runtime and 91.3% on memory consumption.
        :param nums: List of integers, all but one duplicated
        :return: Single non-duplicated integer from input list
        """
        return reduce(xor, nums)
