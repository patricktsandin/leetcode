from operator import sub
from functools import reduce


class Solution:
    """Returns whether a binary tree is height-balanced in O(n) time and
    O(log n) space."""
    def isBalanced(self, root):
        balanced = True
        if root: root.val, root.prev = [], None
        while root and balanced:
            children = list(filter(None, [root.left, root.right]))
            if children:
                for child in children: child.val, child.prev = [], root
                root = children[-1]
            else:
                if not root.val: root.val = [0]
                balanced = abs(reduce(sub, root.val)) <= 1 and balanced
                if root.prev:
                    root.prev.val.append(max(root.val) + 1)
                    if root is root.prev.right: root.prev.right = None
                    if root is root.prev.left: root.prev.left = None
                root = root.prev
        return balanced
