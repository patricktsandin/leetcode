# A square triple (a,b,c) is a triple where a, b, and c are integers and a2 +
# b2 = c2.
#
# Given an integer n, return the number of square triples such that 1 <= a,
# b, c <= n.

from math import sqrt
from functools import cache


class Solution:
    """Solves using recursive algorithm in exponential time and
    linear space."""
    @classmethod
    @cache
    def count_triples(cls, n: int) -> int:
        """Count Pythagorean triples of the form a^2 + b^2 = c^2
        for all values of c between 1 and c given c as n."""
        c = n*n
        triples = 0
        for i in range(9, c//2):
            if sqrt(i).is_integer() and sqrt(c - i).is_integer():
                triples += 2
        return triples + (cls.count_triples(n - 1) if n > 5 else 0)
