"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,
y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""

from typing import Iterator, List
from itertools import chain, islice


class Solution:
    """Solves in linear time and constant space with iterative algorithm
    and iterators."""

    @staticmethod
    def shuffle(nums: List[int], n: int) -> Iterator[int]:
        """Returns generator of interleaved list halves."""
        return chain.from_iterable(
            zip(islice(nums, 0, n), islice(nums, n, None))
        )
