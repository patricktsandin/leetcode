class Solution:
    """Given an integer expressed as an array of digits, increment and return
    as an array of digits.  O(1) space and O(n) time."""
    def plusOne(self, digits):
        for index in range(len(digits) - 1, -1, -1):
            if digits[index] == 9:
                digits[index] = 0
            else:
                digits[index] += 1
                break
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits