"""
You are given two integers, num and t.

An integer x is called achievable if it can become equal to num after
applying the following operation no more than t times:

Increase or decrease x by 1, and simultaneously increase or decrease num by 1.
Return the maximum possible achievable number. It can be proven that there
exists at least one achievable number.
"""


class Solution:
    """Solves in constant time and space"""

    @staticmethod
    def the_maximum_achievable_number(num: int, t: int) -> int:
        """Returns maximum achievable number given a base and
        increments/decrements.
        :param num: Base integer
        :param t: number of increments/decrements to perform
        """
        return num + t*2
