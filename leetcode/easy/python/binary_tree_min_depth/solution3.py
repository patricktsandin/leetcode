class Solution:
    def minDepth(self, root):
        """Returns depth of shallowest leaf node of binary tree in
        O(n) time and O(log n) space using recursive depth-first search."""
        if not root: return 0
        children = [child for child in [root.left, root.right] if child]
        depths = [self.minDepth(child) for child in children]
        root.left = root.right = None
        return min(depths) + 1 if depths else 1
