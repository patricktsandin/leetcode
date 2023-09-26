# You are given a sorted unique integer array nums.
#
# A range [a,b] is the set of all integers from a to b (inclusive).
#
# Return the smallest sorted list of ranges that cover all the numbers in the
# array exactly. That is, each element of nums is covered by exactly one of
# the ranges, and there is no integer x such that x is in one of the ranges
# but not in nums.
#
# Each range [a,b] in the list should be output as:
#
# "a->b" if a != b
# "a" if a == b

from typing import List
from math import inf


class Solution:
    """Summarizes contiguous integer ranges."""
    def summary_ranges(self, nums: List[int]) -> List[str]:
        answer = list()
        nums.append(inf)
        start = end = nums.pop(0)
        for num in nums:
            if num - end == 1:
                end = num
            elif start == end:
                answer.append(f"{start}")
                start = end = num
            elif num - end > 1:
                answer.append(f"{start}->{end}")
                start = end = num
        return answer
