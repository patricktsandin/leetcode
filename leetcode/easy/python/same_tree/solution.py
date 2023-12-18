class Solution:
    def isSameTree(self, p, q):
        """Return whether two provided binary trees are the same in
        O(n) space and O(n) time."""
        return (
            not (p or q)
            or (p and q)
            and p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )
