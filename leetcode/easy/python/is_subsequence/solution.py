class Solution:
    def is_subsequence(self, sub: str, super: str) -> bool:
        """
        Returns whether s is a subsequence of t in linear time and space.
        :param sub: substring
        :param super: superstring
        """
        for char in sub:
            if char in super:
                super = super[super.index(char) + 1:]
            else:
                return False
        return True
