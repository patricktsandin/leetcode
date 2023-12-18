# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

from typing import List
from collections import Counter


class Solution:
    """Solves using iterative algorithm in linear time and space."""
    @staticmethod
    def num_identical_pairs(nums: List[int]) -> int:
        """Count number of 'good pairs' in a list."""
        total = 0
        for count in Counter(nums).values():
            total += (count*(count - 1))//2
        return total
