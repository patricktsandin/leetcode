"""
You're given strings jewels representing the types of stones that are jewels,
and stones representing the stones you have. Each character in stones is a
type of stone you have. You want to know how many of the stones you have are
also jewels.

Letters are case sensitive, so 'a' is considered a different type of stone
from 'A'.
"""

from collections import Counter


class Solution:
    """Solves in linear time and space."""

    @staticmethod
    def num_jewels_in_stones(jewels: str, stones: str) -> int:
        """
        Return count of characters in 'stones' matching those
        in 'jewels'
        :param jewels: Characters to match against
        :param stones: Characters to count
        """
        return Counter(stone for stone in stones if stone in jewels).total()