# Given two integer arrays nums1 and nums2, return an array of their
# intersection. Each element in the result must be unique and you may return
# the result in any order.

from typing import List, Set


class Solution:
    @staticmethod
    def intersection(nums1: List[int], nums2: List[int]) -> Set[int]:
        """Returns intersection of two arrays."""
        return set(nums1) & set(nums2)
