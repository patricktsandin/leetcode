from itertools import zip_longest


class Solution:
    """Gets the longest common prefix from a list of strings in O(n) time
    and O(1) space."""
    def longestCommonPrefix(self, strs):
        for length, letters in enumerate(zip_longest(*strs, fillvalue=None)):
            if not len(set(letters)) == 1:
                return strs[0][:length]
        return strs[0]
