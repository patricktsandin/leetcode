class Solution:
    balanced = True

    def depth(self, root):
        """Return binary tree depth in O(n) time and O(log n) space."""
        depth1 = self.depth(root.left) if root and root.left else 0
        depth2 = self.depth(root.right) if root and root.right else 0
        self.balanced = abs(depth1 - depth2) <= 1 and self.balanced
        return max(depth1, depth2) + 1

    def isBalanced(self, root):
        """Return whether binary tree is height-balanced."""
        self.depth(root) if root else None
        return self.balanced
