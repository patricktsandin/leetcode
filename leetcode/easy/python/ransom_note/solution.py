class Solution:
    """Checks if string 'ransomNote' can be constructed from
    string 'magazine' in O(1) space and O(n) time."""
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_letter_counts = [0]*26
        for letter in ransomNote:
            ransom_letter_counts[ord(letter) - 97] += 1
        magazine_letter_counts = [0]*26
        for letter in magazine:
            magazine_letter_counts[ord(letter) - 97] += 1
        for letter in range(26):
            if magazine_letter_counts[letter] < ransom_letter_counts[letter]:
                return False
        return True
