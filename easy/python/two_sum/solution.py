from bisect import bisect


class Solution:
    """Finds the indices of two numbers in a list that sum to a target number.
    Uses timsort, binary search.  O(n*log n) time, O(n) space."""
    def twoSum(self, nums, target):
        sorted_numbers = sorted(nums)
        if nums.count(target/2) >= 2:
            index1 = nums.index(target/2)
            nums[index1] = None
            index2 = nums.index(target/2)
            return [index1, index2]
        high = bisect(sorted_numbers, target/2)
        low = high - 1
        while low >= 0 and high < len(sorted_numbers):
            total = sorted_numbers[low] + sorted_numbers[high]
            if total > target:
                low -= 1
            elif total < target:
                high += 1
            elif total == target:
                index1 = nums.index(sorted_numbers[low])
                index2 = nums.index(sorted_numbers[high])
                return [index1, index2]
