class Solution:
    """Returns middle node of a linked list (or second middle node)
    in O(n) time and O(1) space."""
    def middleNode(self, head):
        fast_node = slow_node = head
        while fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next
        return slow_node
