from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def remove_elements(
        self, head: Optional[ListNode], val: int
    ) -> Optional[ListNode]:
        """
        Return head of a linked list with all nodes matching val removed.
        Recursive algorithm in linear time and space.
        Beats 91% of LeetCoders on compute.
        :param head: Head of linked list possibly containing 'val'
        :param val: Value of nodes to remove
        :return: Head of linked list without nodes of value 'val'
        """
        if head:
            child = self.remove_elements(head.next, val)
            if head.val == val:
                head = child
            else:
                head.next = child
        return head
