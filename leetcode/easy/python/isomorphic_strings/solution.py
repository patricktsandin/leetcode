# Given two strings s and t, determine if they are isomorphic.
#
# Two strings s and t are isomorphic if the characters in s can be replaced
# to get t.
#
# All occurrences of a character must be replaced with another character
# while preserving the order of characters. No two characters may map to the
# same character, but a character may map to itself.
#
# Constraints:
# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.


class Solution:
    """Beats 98.16% of LeetCoders on time and 99.85% on space."""
    @staticmethod
    def is_isomorphic(s: str, t: str) -> bool:
        """Returns whether two strings are isomorphic using an iterative
        algorithm in linear time and space."""
        mapping = dict()
        for char1, char2 in zip(s, t):
            if char1 not in mapping.keys():
                if char2 not in mapping.values():
                    mapping[char1] = char2
                else:
                    return False
            elif mapping[char1] != char2:
                return False
        return True
