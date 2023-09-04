class Solution:
    """Get minimum depth of a binary tree in O(n) time and O(n) space."""
    def minDepth(self, root):
        if not root:
            return 0
        queue = [(1, root)]
        while queue:
            depth, node = queue.pop()
            children = list(filter(None, [node.left, node.right]))
            if not children:
                return depth
            for child in children:
                queue.insert(0, (depth + 1, child))
