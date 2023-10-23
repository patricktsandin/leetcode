"""
There are n employees in a company, numbered from 0 to n - 1. Each employee i
has worked for hours[i] hours in the company.
The company requires each employee to work for at least target hours.
You are given a 0-indexed array of non-negative integers hours of length n
and a non-negative integer target.
Return the integer denoting the number of employees who worked at least
target hours.
"""

from typing import List


class Solution:
    """Solves with iterative algorithm in linear time and constant space."""

    @staticmethod
    def employees_who_met_target(hours: List[int], target: int) -> int:
        """Returns number of employees who met target of hours worked."""
        return sum(1 for worked in hours if worked >= target)
