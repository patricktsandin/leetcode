# A square triple (a,b,c) is a triple where a, b, and c are integers and a2 +
# b2 = c2.
#
# Given an integer n, return the number of square triples such that 1 <= a,
# b, c <= n.

from math import sqrt


class Solution:
    @staticmethod
    def count_triples(n: int) -> int:
        triples = 0
        while n > 4:
            if n % 2 != 0 and sqrt(n**2 - (n - 1)**2).is_integer():
                triples += 2
            if n > 5 and sqrt(n**2 - (n - 2)**2).is_integer():
                triples += 2
            n -= 1
        return triples
