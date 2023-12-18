"""
We are given a list nums of integers representing a list compressed with
run-length encoding.
Consider each adjacent pair of elements [freq, val] = [nums[2*i],
nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with
value val concatenated in a sublist. Concatenate all the sublists from left
to right to generate the decompressed list.
Return the decompressed list.

Constraints:
2 <= nums.length <= 100
nums.length % 2 == 0
1 <= nums[i] <= 100
"""


from unittest import TestCase
from typing import List, Iterator


class Solution:
    """Solves in linear time and constant space."""

    @staticmethod
    def decompress_rle_list(nums: List[int]) -> Iterator[int]:
        """
        Decompresses a list compressed with run-length encoding
        :param nums: The compressed list of count,value pairs.
        :return: The decompressed list
        """
        assert len(nums) >= 2 and len(nums) % 2 == 0

        nums_iterable = iter(nums)
        for _ in range(len(nums) // 2):
            count = next(nums_iterable)
            val = next(nums_iterable)

            assert val > 0 and count > 0

            for _ in range(count):
                yield val


class TestDecompression(TestCase):
    def test_minimums(self):
        expected = [1]
        result = Solution.decompress_rle_list([1, 1])
        self.assertListEqual(expected, list(result))

    def test_typical_1(self):
        expected = [2, 4, 4, 4]
        result = Solution.decompress_rle_list([1, 2, 3, 4])
        self.assertListEqual(expected, list(result))

    def test_typical_2(self):
        expected = [1, 3, 3]
        result = Solution.decompress_rle_list([1, 1, 2, 3])
        self.assertListEqual(expected, list(result))
