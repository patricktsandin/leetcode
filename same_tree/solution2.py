class Solution:
    def isSameTree(self, p, q):
        """Return whether two provided binary trees are the same in
        O(n * log n) space and O(n) time."""
        stack = [(p, q)]
        while stack:
            p, q = stack.pop()
            if bool(p) != bool(q):
                return False
            if p and q:
                stack.append((p.left, q.left))
                stack.append((p.right, q.right))
                if p.val != q.val:
                    return False
        return True
