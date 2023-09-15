from typing import Optional, List


VISITED = True
NOT_VISITED = False


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
        'post-order traversal'.  Iterative algorithm in linear time and space.
        Beats 95.27% of LeetCoders on memory utilization.  Optimized for
        readability and speed.
        :param root: Root node of a binary tree
        :return: List of node values
        """
        result = []
        if root:
            stack = [(NOT_VISITED, root)]
            while stack:
                visited, node = stack.pop()
                children = list(filter(None, [node.right, node.left]))
                if not visited and children:
                    stack.append((VISITED, node))
                    for child in children:
                        stack.append((NOT_VISITED, child))
                else:
                    result.append(node.val)
        return result
