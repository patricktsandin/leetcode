class Solution:
    def hasPathSum(self, root, targetSum):
        """Returns whether a binary tree contains a complete path which sums
        to a target value.  Recursive depth-first-search algorithm in
        O(log n) space and O(n) time."""
        return root and (
            root.left and self.hasPathSum(root.left, targetSum - root.val)
            or root.right and self.hasPathSum(root.right, targetSum - root.val)
            or not (root.left or root.right) and targetSum == root.val
        )
