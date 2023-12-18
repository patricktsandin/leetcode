"""
There are n kids with candies. You are given an integer array candies,
where each candies[i] represents the number of candies the ith kid has,
and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if,
after giving the ith kid all the extraCandies, they will have the greatest
number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.
"""

from typing import List, Iterator
from unittest import TestCase


class Solution:
    """Solves iteratively in linear time and constant space."""

    @staticmethod
    def kids_with_candies(
        candies: List[int], extra_candies: int
    ) -> Iterator[bool]:
        """
        Returns a boolean array denoting which kids from the input
        have the most candies if granted an extra stash.
        :param candies: starting supply of candies for each kid
        :param extra_candies: extra stash of candies for one kid
        :return: list of kids who could end up with the most candies
        """
        max_candies = max(candies)
        return (candy + extra_candies >= max_candies for candy in candies)


class MaxCandiesTest(TestCase):
    def test_minimum_candies(self) -> None:
        expected = [True, True, True]
        result = Solution.kids_with_candies([1, 1, 1], 1)
        self.assertSequenceEqual(expected, list(result))

    def test_ascending_candies_with_few_extras(self) -> None:
        expected = [False, True, True]
        result = Solution.kids_with_candies([1, 2, 3], 1)
        self.assertSequenceEqual(expected, list(result))

    def test_ascending_candies_with_many_extras(self) -> None:
        expected = [True, True, True]
        result = Solution.kids_with_candies([1, 2, 3], 5)
        self.assertSequenceEqual(expected, list(result))
