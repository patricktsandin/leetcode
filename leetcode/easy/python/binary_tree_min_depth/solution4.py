class Solution:
    """Returns depth of shallowest leaf node of binary tree in
    O(n) time and O(1) space using iterative depth-first search.  No stack: uses
    the tree itself for storage, deleting subtrees as it goes."""
    def minDepth(self, root):
        if not root:
            return 0
        while True:
            if root.left and not isinstance(root.left, int):
                root.left.val = root
                root = root.left
            elif root.right and not isinstance(root.right, int):
                root.right.val = root
                root = root.right
            else:
                depths = [
                    depth for depth in [root.left, root.right]
                    if isinstance(depth, int)
                ]
                if not isinstance(root.val, int):
                    if root.val.right is root:
                        root.val.right = min(depths) + 1 if depths else 2
                    if root.val.left is root:
                        root.val.left = min(depths) + 1 if depths else 2
                    root = root.val
                else:
                    return min(depths) if depths else 1
