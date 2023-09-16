class Solution:
    def inorderTraversal(self, root):
        """Returns the left-to-right order of values in a binary tree with
        recursion in O(n) time and O(n) space."""
        result = []
        if root:
            if root.left:
                result.extend(self.inorderTraversal(root.left))
                root.left = None
            result.append(root.val)
            if root.right:
                result.extend(self.inorderTraversal(root.right))
                root.right = None
        return result
