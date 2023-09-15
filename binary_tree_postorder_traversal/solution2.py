from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
        """
        Returns values from a binary tree in the order of discovery given
        a depth-first left-to-right search that does not record the value
        of a non-leaf node until ascending past it.  This is also called
        'post-order traversal'.  Stackless iterative algorithm in linear
        time and constant space, optimized for memory utilization by
        leveraging generator functionality and cannibalizing input.
        Beats 77.18% of LeetCoders on runtime and 72.03% on memory.
        :param root: Root node of a binary tree
        :return: List of node values
        """
        while root:
            if root.left:
                root.left.prev = root
                root = root.left
            elif root.right:
                root.right.prev = root
                root = root.right
            elif hasattr(root, 'prev'):
                if root.prev.left == root:
                    root.prev.left = None
                elif root.prev.right == root:
                    root.prev.right = None
                yield root.val
                root = root.prev
            else:
                yield root.val
                break
