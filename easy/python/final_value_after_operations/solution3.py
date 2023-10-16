"""
There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return
the final value of X after performing all the operations.
"""

from typing import List


class Solution:
    """Solves with iterative algorithm in linear time and space."""

    @staticmethod
    def final_value_after_operations(operations: List[str]) -> int:
        """Applies operations to variable initialized to 0."""
        return sum([1 if "+" in n else -1 for n in operations])
