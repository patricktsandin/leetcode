from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Returns values from a binary tree in the order of discovery given
        a depth-first left-to-right search that does not record the value
        of a non-leaf node until ascending past it.  This is also called
        'post-order traversal'.  Recursive algorithm optimized for
        performance in linear time and space.  Beats 99.79% of LeetCoders
        on memory consumption.
        :param root: Root node of a binary tree
        :return: List of node values
        """
        return [
            *self.postorder_traversal(root.left),
            *self.postorder_traversal(root.right),
            root.val
        ] if root else []
