from collections import Counter


class Solution:
    """Detects if string of ints contains duplicates in O(n) time and
    O(n) space."""
    def containsDuplicate(self, nums):
        return max(Counter(nums).values()) > 1
