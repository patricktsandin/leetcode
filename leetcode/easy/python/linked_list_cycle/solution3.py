class Solution:
    def hasCycle(self, head):
        """Returns whether a linked list has a cycle in O(n) time and O(1)
        space."""
        lookahead = head
        while head and head.next and lookahead and lookahead.next:
            head, lookahead = head.next, lookahead.next.next
            if head == lookahead:
                return True
        return False
