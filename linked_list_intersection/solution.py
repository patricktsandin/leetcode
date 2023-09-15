from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def get_intersection_node(
        head1: ListNode, head2: ListNode
    ) -> Optional[ListNode]:
        """
        Returns node where two linked lists intersect using iterative algorithm
        in linear space and exponential time.
        :param head1: Head of a linked list
        :param head2: Head of a linked list
        :return: Node where two lists intersect
        """
        set1, set2 = set(), set()
        while head1 or head2:
            if head1:
                set1.add(head1)
                head1 = head1.next
            if head2:
                set2.add(head2)
                head2 = head2.next
            if set1 & set2:
                return (set1 & set2).pop()
        return None
