from typing import List
from collections import Counter


class Solution:
    @staticmethod
    def single_number(nums: List[int]) -> int:
        """
        Given a list where all elements are duplicates except one, return
        the singular element.  O(n) space and O(n) time, iterative algorithm.
        Beats 88.4% of LeetCoders on runtime.
        :param nums: List of integers, all but one duplicated
        :return: Single non-duplicated integer from input list
        """
        return Counter(nums).most_common()[-1][0]
