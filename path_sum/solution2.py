class Solution:
    def hasPathSum(self, root, targetSum):
        """Returns whether a binary tree contains a complete path which sums
        to a target value.  Iterative depth-first-search algorithm in O(n)
        time and O(log n) space.  Space complexity is nearly O(1) except
        for the addition of a parent node pointer."""
        if not root:
            return False
        root.prev = None
        while root:
            children = list(filter(None, [root.left, root.right]))
            if children:
                children[0].prev = root
                children[0].val += root.val
                root = children[0]
            else:
                if root.val == targetSum:
                    return True
                if root.prev:
                    if root.prev.right is root:
                        root.prev.right = None
                    elif root.prev.left is root:
                        root.prev.left = None
                    if not (root.prev.left or root.prev.right):
                        root.prev.val = None
                root = root.prev
        return False
