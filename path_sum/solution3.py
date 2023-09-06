class Solution:
    def hasPathSum(self, root, targetSum):
        """Returns whether a binary tree contains a complete path which sums
        to a target value.  Recursive depth-first-search algorithm in
        O(log n) space and O(n) time."""
        if root:
            children = list(filter(None, [root.left, root.right]))
            if not children:
                return targetSum == root.val
            else:
                return any([
                    self.hasPathSum(child, targetSum - root.val)
                    for child in children
                ])