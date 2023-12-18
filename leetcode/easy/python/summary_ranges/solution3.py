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


class Solution:
    """Summarizes contiguous integer ranges."""
    @staticmethod
    def summary_ranges(nums: List[int]) -> List[str]:
        ranges = []
        for num in nums:
            if ranges and ranges[-1][1] == num - 1:
                ranges[-1][1] = num
            else:
                ranges.append([num, num])
        return [
            f"{beginning}->{end}" if beginning != end
            else f"{beginning}"
            for beginning, end in ranges
        ]
