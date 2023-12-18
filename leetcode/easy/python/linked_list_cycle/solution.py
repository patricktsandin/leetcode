class Solution:
    def hasCycle(self, head):
        """Returns whether a linked list has a cycle in O(n) time and O(1)
        space."""
        while head and head.next:
            if head.val is None:
                return True
            head.val = None
            head = head.next
        return False