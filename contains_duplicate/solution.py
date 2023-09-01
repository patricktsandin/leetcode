from collections import Counter


class Solution:
    """Detects if a string of integers contains duplicates in O(n) time and
    O(n) space."""
    def containsDuplicate(self, nums):
        return max(Counter(nums).values()) > 1
