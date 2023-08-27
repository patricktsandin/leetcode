class Solution:
    """Detects if string of ints contains duplicates in O(n) time and
    O(1) space."""
    def containsDuplicate(self, nums):
        counts = set()
        while nums:
            num = nums.pop()
            if num in counts:
                return True
            else:
                counts.add(num)
        return False
