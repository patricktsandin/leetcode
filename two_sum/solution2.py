class Solution:
    """Finds the indices of two numbers in a list that sum to a target number.
    Uses timsort, binary search.  O(n*log n) time, O(n) space."""
    def twoSum(self, nums, target):
        sorted_numbers = sorted(nums)
        high = len(nums) - 1
        low = 0
        while low < high:
            total = sorted_numbers[low] + sorted_numbers[high]
            if total < target:
                low += 1
            elif total > target:
                high -= 1
            elif total == target:
                index1 = nums.index(sorted_numbers[low])
                nums[index1] = None
                index2 = nums.index(sorted_numbers[high])
                return [index1, index2]
