class Solution:
    """Moves all zeros to end of list in-place in O(1) space and O(n) time.
    Made slightly faster per line_profiler by removing try-except."""
    def moveZeroes(self, nums):
        zeroes = 0
        length = len(nums)
        index = 0
        while index < length:
            if nums[index] == 0:
                nums.pop(index)
                zeroes += 1
                length -= 1
            else:
                index += 1
        nums.extend([0]*zeroes)