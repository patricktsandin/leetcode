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
    def contains_nearby_duplicate(self, nums: List[int], k: int) -> bool:
        """
        Returns whether list nums contains any duplicates within a sliding
        window of length k+1 in subquadratic time and quadratic space
        using a naieve recursive algorithm.
        """
        return (
            len(set(nums[:k + 1])) < len(nums[:k + 1])
            or self.contains_nearby_duplicate(nums[1:], k)
        ) if nums and k else False
