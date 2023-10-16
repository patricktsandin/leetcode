"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,
y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""

from typing import List, Iterator


class Solution:
    """Solves in linear time and constant space with iterative algorithm
    and generator."""

    @staticmethod
    def shuffle(nums: List[int], n: int) -> Iterator[int]:
        """Returns generator of interleaved list halves."""
        for i, num in enumerate(nums):
            if i == n:
                break
            yield num
            yield nums[n + i]
