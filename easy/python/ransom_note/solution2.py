from collections import Counter


class Solution:
    """Checks if string 'ransomNote' can be constructed from
    string 'magazine' in O(1) space and O(n) time."""
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return Counter(magazine) >= Counter(ransomNote)
