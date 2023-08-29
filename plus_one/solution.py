class Solution:
    """Given an integer expressed as an array of digits, increment and
    return as an array of digits.  O(1) space and O(n) time."""
    def plusOne(self, digits):
        carry = 1
        for index in range(-1, -(len(digits) + 1), -1):
            if digits[index] + carry > 9:
                digits[index] = 0
                carry = 1
            else:
                digits[index] += carry
                carry = 0
                break
        if carry:
            digits.insert(0, carry)
        return digits
