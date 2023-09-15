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
        in linear space and linear time.
        :param head1: Head of a linked list
        :param head2: Head of a linked list
        :return: Node where two lists intersect
        """
        while head1 or head2:
            if head1:
                if hasattr(head1, 'visited'):
                    return head1
                else:
                    head1.visited = True
                    head1 = head1.next
            if head2:
                if hasattr(head2, 'visited'):
                    return head2
                else:
                    head2.visited = True
                    head2 = head2.next
        return None
