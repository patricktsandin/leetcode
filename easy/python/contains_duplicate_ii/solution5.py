"""
Given an integer array nums and an integer k, return true if there are two
distinct indices i and j in the array such that nums[i] == nums[j] and abs(
i - j) <= k.

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""

from typing import List
from itertools import islice


class Solution:
    """Solves using an iterative algorithm in subquadratic/multilinear
    O(len(nums)*k) time and linear O(k) space."""

    @staticmethod
    def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
        """
        Returns whether list nums contains any duplicates within a sliding
        window of length k+1.
        """
        window_size = min([k + 1, len(nums)])
        window = set(nums[:window_size - 1])
        window_start = iter(nums)
        window_end = islice(iter(nums), window_size - 1, None)
        for new, old in zip(window_end, window_start):
            window.add(new)
            if len(window) < window_size:
                return True
            window.remove(old)
        return False
