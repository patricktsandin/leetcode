class Solution:
    """Remove val from nums in-place and return length of nums in
    O(n) time and O(n) space."""
    def removeElement(self, nums, val):
        nums[:] = [num for num in nums if num != val]
        return len(nums)
