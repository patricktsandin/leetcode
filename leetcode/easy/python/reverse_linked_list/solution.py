from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def reverse_list(node1: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a linked list iteratively in linear time and constant space.
        :param node1: Head of a linked list
        :return: Head of reversed linked list
        """
        if node1:
            node2, node1.next = node1.next, None
            while node2:
                node1, node2.next, node2 = node2, node1, node2.next
        return node1
