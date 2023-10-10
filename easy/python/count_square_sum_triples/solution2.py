# A square triple (a,b,c) is a triple where a, b, and c are integers and a2 +
# b2 = c2.
#
# Given an integer n, return the number of square triples such that 1 <= a,
# b, c <= n.

from itertools import combinations


class Solution:
    """Solves using iterative algorithm in linear time and space."""
    @staticmethod
    def count_triples(n: int) -> int:
        """
        Count Pythagorean triples of the form a^2 + b^2 = {1..n}^2
        :param n: Third element of a Pythagorean Triple
        :return: Count of all Pythagorean triples ending in an integer
        between 1 and n.
        """
        squares = {number**2 for number in range(1, n + 1)}
        pairs = combinations(squares, 2)
        triples_count = 0
        for pair in pairs:
            if sum(pair) in squares:
                triples_count += 2
        return triples_count
