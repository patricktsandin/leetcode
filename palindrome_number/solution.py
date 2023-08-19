class Solution:
    """Checks if an integer is a palindrome in O(n) time and O(n) space."""
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        for position in range(len(string)//2):
            if string[position] != string[-(position + 1)]:
                return False
        return True
