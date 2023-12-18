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
    @staticmethod
    def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
        """
        Returns whether list nums contains any duplicates within a sliding
        window of length k+1 in linear time and space using an iterative
        algorithm.
        """
        visited = dict()
        for index, num in enumerate(nums):
            if num not in visited:
                visited[num] = index
            elif abs(visited[num] - index) <= k:
                return True
            else:
                visited[num] = index
        return False
