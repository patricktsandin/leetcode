class Solution:
    """Finds the indices of two numbers in a list that sum to a target number.
    O(n) time, O(n) space."""
    def twoSum(self, nums, target):
        indexes_by_value = {}
        for index, number in enumerate(nums):
            difference = target - number
            if difference in indexes_by_value:
                return [index, indexes_by_value[difference]]
            indexes_by_value[number] = index
