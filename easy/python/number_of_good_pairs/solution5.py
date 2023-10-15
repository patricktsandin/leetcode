"""
Given an array of integers nums, return the number of good pairs.
A pair (i, j) is called good if nums[i] == nums[j] and i < j.
"""

from typing import List
from collections import Counter
from math import comb


class Solution:
    """Solves using iterative algorithm in linear time and space."""

    @staticmethod
    def num_identical_pairs(nums: List[int]) -> int:
        """Count number of 'good pairs' in a list."""
        return sum(map(lambda n: comb(n, 2), Counter(nums).values()))
