from math import log10


class Solution:
    """Checks if an integer is a palindrome in O(n) time and O(1) space
    *without converting to string*."""
    class Solution:
        def isPalindrome(self, x: int) -> bool:
            if x < 0:
                return False
            length = int(log10(x or 1)) + 1
            for index in range(1, length//2 + 1):
                if not (
                    x // 10**(length - index) % 10
                    == x % 10**index // 10**(index - 1)
                ):
                    return False
            return True
