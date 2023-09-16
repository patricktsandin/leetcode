class Solution:
    """Detects if string of ints contains duplicates in O(n) time and
    O(n) space."""
    def containsDuplicate(self, nums):
        counts = {}
        for num in nums:
            if num in counts:
                return True
            else:
                counts[num] = 1
        return False
