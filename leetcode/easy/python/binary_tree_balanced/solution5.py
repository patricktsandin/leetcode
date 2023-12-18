from operator import sub
from functools import reduce


class Solution:
    """Returns whether a binary tree is height-balanced in O(n) time and
    O(1) space."""
    def isBalanced(self, root):
        balanced = True
        while root and not isinstance(root, int) and balanced:
            children = [
                child for child in [root.left, root.right]
                if child and not isinstance(child, int)
            ]
            if children:
                for child in children: child.val = root
                root = children[-1]
            else:
                depths = [
                    depth for depth in [root.left, root.right, 0]
                    if isinstance(depth, int)
                ]
                balanced = abs(reduce(sub, depths)) <= 1 and balanced
                if not isinstance(root.val, int):
                    if root is root.val.right: root.val.right = max(depths) + 1
                    if root is root.val.left: root.val.left = max(depths) + 1
                root = root.val
        return balanced
