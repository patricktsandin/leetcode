"""
There is a hidden integer array arr that consists of n non-negative integers.
It was encoded into another integer array encoded of length n - 1, such that
encoded[i] = arr[i] XOR arr[i + 1]. For example, if arr = [1,0,2,1],
then encoded = [1,2,3].
You are given the encoded array. You are also given an integer first, that is
the first element of arr, i.e. arr[0].
Return the original array arr. It can be proved that the answer exists and is
unique.

Constraints:
2 <= n <= 104
encoded.length == n - 1
0 <= encoded[i] <= 105
0 <= first <= 105
"""


from unittest import TestCase
from typing import List, Iterator
from itertools import chain


class Solution:
    """Solves iteratively in linear time and constant space."""

    @staticmethod
    def decode(encoded: List[int], first: int) -> Iterator[int]:
        """
        Reverses the pairwise xor-ing of an array, given the xor'd array
        and the first integer of the original array.
        :param encoded: the result of pairwise xor-ing an array
        :param first: the first integer of the original array
        :return: the original array
        """
        assert first >= 0
        assert len(encoded) > 0

        current = first

        for integer in chain((0,), encoded):
            yield (current := current ^ integer)


class TestDecode(TestCase):
    def test_minimum(self):
        expected = [0, 0]
        result = Solution.decode([0], 0)
        self.assertListEqual(expected, list(result))

    def test_repeating(self):
        expected = [3, 3, 3, 3, 3]
        result = Solution.decode([0, 0, 0, 0], 3)
        self.assertListEqual(expected, list(result))

    def test_typical_1(self):
        expected = [1, 0, 2, 1]
        result = Solution.decode([1, 2, 3], 1)
        self.assertListEqual(expected, list(result))

    def test_typical_2(self):
        expected = [4, 2, 0, 7, 4]
        result = Solution.decode([6, 2, 7, 3], 4)
        self.assertListEqual(expected, list(result))
