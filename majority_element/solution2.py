class Solution:
    """Returns majority element in O(1) space and O(n) time with
    Boyer-Moore voting algorithm."""
    def majorityElement(self, nums):
        count = 1
        candidate = nums[0]
        for digit in nums[1:]:
            if digit == candidate:
                count += 1
            else:
                count -= 1
            if count == 0:
                candidate = digit
                count = 1
        return candidate
