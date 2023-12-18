import re


class Solution:
    def repeatedSubstringPattern(self, s):
        """Returns whether a string is composed of repeated substrings"""
        return bool(re.fullmatch(r"^(.+)\1+$", s))
