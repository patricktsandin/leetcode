class Solution:
    def balance_and_depth(self, root):
        """Return binary tree depth in O(n) time and O(log n) space."""
        depth1 = depth2 = 0
        balanced1 = balanced2 = True
        if root:
            if root.right:
                balanced1, depth1 = self.balance_and_depth(root.right)
            if root.left:
                balanced2, depth2 = self.balance_and_depth(root.left)
        balanced = abs(depth1 - depth2) <= 1 and balanced1 and balanced2
        max_depth = max(depth1, depth2) + 1
        return balanced, max_depth

    def isBalanced(self, root):
        """Return whether binary tree is height-balanced."""
        return self.balance_and_depth(root)[0]
