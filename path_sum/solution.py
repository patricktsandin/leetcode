class Solution:
    def hasPathSum(self, root, targetSum):
        """Returns whether a binary tree contains a complete path which sums
        to a target value.  Iterative depth-first-search algorithm in O(n)
        time and O(log n) space."""
        if not root:
            return False
        stack = [(root.val, root)]
        while stack:
            total, node = stack.pop()
            children = list(filter(None, [node.left, node.right]))
            if not children and total == targetSum:
                return True
            for child in children:
                stack.append((total + child.val, child))
