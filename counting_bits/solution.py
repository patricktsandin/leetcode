class Solution:
    """Given an integer n, returns an array of the number of bits in the
    binary representation of every integer between 0 and n in O(n) space and
    O(n) time."""
    def countBits(self, n):
        result = []
        for integer in range(n + 1):
            result.append(integer.bit_count())
        return result
