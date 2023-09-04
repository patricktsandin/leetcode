class Solution:
    """Moves all zeros to end of list in-place in O(1) space and O(n) time."""
    def moveZeroes(self, nums):
        length = len(nums)
        index = 0
        while index < length:
            try:
                if nums[index] == 0:
                    nums.pop(index)
                    continue
            except IndexError:
                nums.append(0)
            index += 1
