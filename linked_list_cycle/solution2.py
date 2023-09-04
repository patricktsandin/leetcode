class Solution:
    def hasCycle(self, head):
        """Returns whether a linked list has a cycle in O(n) time and O(1)
        space."""
        while head and head.next is not None:
            if head.next is False:
                return True
            next = head.next
            head.next = False
            head = next
        return False