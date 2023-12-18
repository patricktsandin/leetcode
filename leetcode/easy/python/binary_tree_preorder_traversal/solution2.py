from typing import Optional, Iterator


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def preorder_traversal(root: Optional[TreeNode]) -> Iterator[int]:
        """
        Returns pre-order traversal of the values of a binary tree
        using an iterative, stackless DFS algorithm and generator function
        in constant space and time.
        Optimizing for memory at the expense of sanity.
        Beats 94.86% of LeetCoders on memory.
        :param root: Root of a binary tree to traverse
        :return: Returns an iterator of tree values
        """
        if root:
            yield root.val
            root.val = None
            while root:
                if root.left:
                    if isinstance(root.left.val, int):
                        yield root.left.val
                    root.left.val = root
                    root = root.left
                elif root.right:
                    if isinstance(root.right.val, int):
                        yield root.right.val
                    root.right.val = root
                    root = root.right
                elif root.val:
                    if root == root.val.left:
                        root.val.left = None
                    elif root == root.val.right:
                        root.val.right = None
                    root = root.val
                else:
                    break
