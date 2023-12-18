# Given two integer arrays nums1 and nums2, return an array of their
# intersection. Each element in the result must be unique and you may return
# the result in any order.

from typing import List


class Solution:
    @staticmethod
    def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
        """Returns intersection of two arrays."""
        return [
            num for num in dict.fromkeys(nums1)
            if num in dict.fromkeys(nums2)
        ]
