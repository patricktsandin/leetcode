"""
You are given a 0-indexed integer array nums and an integer k.
Return an integer that denotes the sum of elements in nums whose
corresponding indices have exactly k set bits in their binary representation.
The set bits in an integer are the 1's present when it is written in binary.
For example, the binary representation of 21 is 10101, which has 3 set bits.
"""

from unittest import TestCase
from typing import List


class Solution:
    """Solves iteratively in constant space and linear time."""

    @staticmethod
    def sum_indices_with_k_set_bits(numbers: List[int], bit_count: int) -> int:
        """
        Sums list items whose indices contain an exact number of bits.
        :param numbers: list of items
        :param bit_count: number of bits incides must contain exactly
        :return: sum of matched items
        """
        assert 1 <= len(numbers) <= 1000
        assert 0 <= bit_count <= 10

        return sum(
            number
            for i, number in enumerate(numbers)
            if i.bit_count() == bit_count
        )


class TestSumIndicesWithKSetBits(TestCase):
    def test_minimum_input(self):
        expected = 0
        result = Solution.sum_indices_with_k_set_bits([0], 0)
        self.assertEqual(expected, result)

    def test_typical_input_1(self):
        expected = 2
        result = Solution.sum_indices_with_k_set_bits([1, 0, 1, 0, 1, 0], 1)
        self.assertEqual(expected, result)

    def test_typical_input_2(self):
        expected = 2
        result = Solution.sum_indices_with_k_set_bits([5, 4, 3, 2, 1, 0], 2)
        self.assertEqual(expected, result)

    def test_typical_input_3(self):
        expected = 0
        result = Solution.sum_indices_with_k_set_bits([0, 1, 2, 3, 4, 5], 10)
        self.assertEqual(expected, result)
