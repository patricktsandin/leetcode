class Solution:
    def maxDepth(self, root):
        """Return maximum depth of binary tree in O(n) time and
        O(n * log n) space."""
        max_depth = 0
        if root:
            stack = [(1, root)]
            while stack:
                depth, node = stack.pop()
                if depth > max_depth:
                    max_depth = depth
                stack.extend(
                    [
                        (depth + 1, new_node)
                        for new_node in [node.left, node.right]
                        if new_node
                    ]
                )
        return max_depth
