# Given an integer n, return true if it is a power of two. Otherwise, return
# false.

class Solution:
    """Returns whether an integer is a power of two"""
    @staticmethod
    def is_power_of_two(n: int) -> bool:
        return not n & (n - 1) and n
