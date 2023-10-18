"""
You are given an m x n integer grid accounts where accounts[i][j] is the
amount of money the ith customer has in the jth
bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank
accounts. The richest customer is the customer that has the maximum wealth.
"""

from typing import List


class Solution:
    """Solves with iterative algorithm in linear time and constant space."""

    @staticmethod
    def maximum_wealth(accounts: List[List[int]]) -> int:
        """Return sum of largest row in matrix."""
        return max(sum(account) for account in accounts)
