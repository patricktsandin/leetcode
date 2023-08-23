import re


class Solution:
    """Checks whether or not a set of grouping symbols is appropriately
    matched in a given string"""
    def isValid(self, s):
        while re.search(r'\{\}|\(\)|\[\]', s):
            s = re.sub(r'\{\}|\(\)|\[\]', '', s)
        return not bool(s)
