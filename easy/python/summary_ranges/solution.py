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
    @staticmethod
    def summary_ranges(nums: List[int]) -> List[str]:
        if not nums:
            return list()

        ranges = []
        current_range = None
        answer = []
        for num in nums:
            if not current_range:
                current_range = [num]
            elif abs(num - current_range[-1]) > 1:
                ranges.append(current_range)
                current_range = [num]
            else:
                current_range.append(num)
        ranges.append(current_range)
        for range_ in ranges:
            if len(range_) == 1:
                answer.append(f"{range_[0]}")
            else:
                answer.append(f"{range_[0]}->{range_[-1]}")
        return answer
