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
    """Solves with iterative algorithm in linear time and constant space."""

    @staticmethod
    def final_value_after_operations(operations: List[str]) -> int:
        """Applies operations to variable initialized to 0."""

        x = 0
        operator_from_operation = {
            "++X": lambda n: n + 1,
            "X++": lambda n: n + 1,
            "--X": lambda n: n - 1,
            "X--": lambda n: n - 1
        }
        for operation in operations:
            x = operator_from_operation[operation](x)
        return x
