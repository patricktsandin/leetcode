from bisect import bisect_left


class Solution:
    """Return position or insert position of element in list in
    O(n * log n) time and O(1) space."""
    def searchInsert(self, nums, target):
        return bisect_left(nums, target)
