from operator import sub
from functools import reduce


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root):
        balanced = True
        if root:
            stack: list = [root]
            root.depths = []
            root.prev = None
            while stack and balanced:
                node = stack[-1]
                children = list(filter(None, [node.left, node.right]))
                if children:
                    for child in children:
                        child.prev = node
                        child.depths = []
                    stack.extend(children)
                    continue
                else:
                    stack.pop()
                    if len(node.depths) == 2:
                        breakpoint()
                        balanced = abs(
                            reduce(sub, node.depths)
                        ) <= 1 and balanced
                    if node.depths and node.prev:
                        node.prev.depths.append(max(node.depths) + 1)
                    if node.prev and node is node.prev.right:
                        node.prev.right = None
                    if node.prev and node is node.prev.left:
                        node.prev.left = None
        return balanced


tree = TreeNode(
    right=TreeNode(
        right=TreeNode(),
        left=TreeNode(
            right=TreeNode(),
            left=TreeNode(
                right=TreeNode(),
                left=TreeNode()
            )
        )
    ),
    left=TreeNode()
)

print(
    Solution().isBalanced(tree)
)
