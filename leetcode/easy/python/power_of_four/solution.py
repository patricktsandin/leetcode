# Given an integer n, return true if it is a power of four. Otherwise,
# return false.

class Solution:
    """Beats 94.86% of LeetCoders on compute and 81.87% on memory."""
    @staticmethod
    def is_power_of_four(n: int) -> bool:
        """Checks if an integer n is a power of 4."""
        return n and not n & (n - 1) and n.bit_length() % 2 != 0
