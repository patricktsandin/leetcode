class Solution:
    def twoSum(self, nums, target):
        for index, number in enumerate(nums):
            complement = target - number
            if complement in nums and index != nums.index(complement):
                return index, nums.index(complement)
