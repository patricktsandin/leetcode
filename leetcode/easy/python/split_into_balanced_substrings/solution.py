"""
Balanced strings are those that have an equal quantity of 'L' and 'R'
characters.
Given a balanced string s, split it into some number of substrings such that:
Each substring is balanced.
Return the maximum number of balanced strings you can obtain.

2 <= s.length <= 1000
s[i] is either 'L' or 'R'.
s is a balanced string.
"""


from unittest import TestCase


class Solution:
    """Solves in linear time and constant space."""

    @staticmethod
    def balanced_string_split(string: str) -> int:
        """
        Count the non-overlapping substrings which contain the
        same number of Ls and Rs.
        :param string: string to split
        :return: number of strings that can be derived
        """
        assert len(string) >= 2 and len(string) % 2 == 0

        balance = 0
        count = 0
        for character in string:
            if character == "R":
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                count += 1
        return count


class TestBalancedStringSplit(TestCase):
    def test_typical_1(self):
        expected = 4
        result = Solution.balanced_string_split("RLRRLLRLRL")
        self.assertEqual(expected, result)

    def test_typical_2(self):
        expected = 2
        result = Solution.balanced_string_split("RLRRRLLRLL")
        self.assertEqual(expected, result)

    def test_typical_3(self):
        expected = 1
        result = Solution.balanced_string_split("LLLLRRRR")
        self.assertEqual(expected, result)
