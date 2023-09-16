class Solution:
    def isSymmetric(self, root):
        """Returns whether a binary tree is symmetrical in
        O(n) time and O(n * log n) space."""
        stack = [(root.left, root.right)]
        while stack:
            node1, node2 = stack.pop()
            if node1 and node2 and node1.val == node2.val:
                stack.extend([
                    (node1.left, node2.right),
                    (node2.left, node1.right)
                ])
            elif not (node1 or node2):
                continue
            else:
                return False
        return True
