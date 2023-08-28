from math import sqrt


class Solution:
    """Calculate number of distinct ways to climb a set of n stairs with a
     stride varying between 1 and 2 steps.  O(1) time, O(1) space."""
    def climbStairs(self, n):
        n += 1
        sqrt5 = sqrt(5)
        phi = (sqrt5 + 1) / 2
        return int(
            (phi**n - (1 - phi)**n) / sqrt5
        )
