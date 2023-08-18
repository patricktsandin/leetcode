class Solution:
    """Calculate the number of steps to reduce a whole number to 0 using only
    num-1 if num is odd and num/2 if num is even."""
    def numberOfSteps(self, num):
        return num.bit_length() + num.bit_count() - 1 if num else 0
