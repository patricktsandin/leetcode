class Solution:
    def is_symmetric(self, left, right):
        """Returns whether two binary trees are symmetrical in
        O(n) time and O(n * log n) space."""
        return (
                not (left or right)
                or left and right and left.val == right.val
                and self.is_symmetric(left.left, right.right)
                and self.is_symmetric(right.left, left.right)
        )

    def isSymmetric(self, root):
        """Returns whether a binary tree is symmetrical in
        O(n) time and O(n * log n) space."""
        return self.is_symmetric(root.left, root.right)
