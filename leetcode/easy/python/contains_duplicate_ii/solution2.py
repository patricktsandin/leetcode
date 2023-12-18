# Given an integer array nums and an integer k, return true if there are two
# distinct indices i and j in the array such that nums[i] == nums[j] and abs(
# i - j) <= k.
#
# Constraints:
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# 0 <= k <= 105

from typing import List


class Solution:
    """Beats 97.46% of LeetCoders on memory usage."""
    @staticmethod
    def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
        """
        Returns whether list nums contains any duplicates within a sliding
        window of length k+1 using an iterative algorithm in
        subquadratic/multilinear O(len(nums)*k) time and linear O(k) space.
        """
        length = len(nums)
        window_size = min([k + 1, length])
        window = set(nums[:window_size - 1])
        for pointer in range(length - window_size + 1):
            window.add(nums[pointer + window_size - 1])
            if len(window) < window_size:
                return True
            window.remove(nums[pointer])
        return False
