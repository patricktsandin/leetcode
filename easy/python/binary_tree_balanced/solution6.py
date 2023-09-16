class Solution:
    def isBalanced(self, root):
        """Return whether child trees are height-balanced and maximum depth
        in O(n) time and O(n) space."""
        if root:
            def depth(root):
                depth1 = depth(root.left) if root.left else 0
                depth2 = depth(root.right) if root.right else 0
                if not abs(depth1 - depth2) <= 1:
                    raise Exception
                return max(depth1, depth2) + 1

            try:
                depth(root)
            except:
                return False
        return True
