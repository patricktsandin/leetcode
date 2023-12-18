class Solution:
    """Moves all zeros to end of list in-place in O(n) space and O(n) time.
    Made slightly faster per line_profiler by removing while loop, index,
    and check at the expense of added memory."""
    def moveZeroes(self, nums):
        length = len(nums)
        nums[:] = [num for num in nums if num != 0]
        nums.extend([0]*(length - len(nums)))
