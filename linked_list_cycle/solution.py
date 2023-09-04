class Solution:
    """Returns whether a linked list has a cycle in O(n) time and O(1) space."""
    def hasCycle(self, head):
        while head and head.next:
            if head.val is None:
                return True
            head.val = None
            head = head.next
        return False