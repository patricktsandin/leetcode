# An ugly number is a positive integer whose prime factors are limited to 2, 3,
# and 5.  Given an integer n, return true if n is an ugly number.

class Solution:
    @staticmethod
    def is_ugly(n: int) -> bool:
        """Return whether integer is ugly using iterative algorithm."""
        while n:
            if n % 2 == 0:
                n //= 2
            elif n % 3 == 0:
                n //= 3
            elif n % 5 == 0:
                n //= 5
            else:
                break
        return n == 1
