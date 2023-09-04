class Solution:
    def minDepth(self, root):
        """Get minimum depth of a binary tree in O(n) time and O(log n) space
        using iterative depth-first search with a stack."""
        if not root:
            return 0
        min_depth = -1
        stack = [(1, root)]
        while stack:
            depth, node = stack.pop()
            children = list(filter(None, [node.left, node.right]))
            if not children and (depth < min_depth or min_depth < 0):
                min_depth = depth
            for child in children:
                stack.append((depth + 1, child))
        return min_depth