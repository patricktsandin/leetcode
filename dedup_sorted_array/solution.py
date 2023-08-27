class Solution:
    """Deduplicates a provided array in-place and returns its length in
    O(n) space and O(n * log n) time"""
    def removeDuplicates(self, nums):
        nums[:] = set(nums)
        nums.sort()
        return len(nums)
