from typing import Optional, Tuple


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def get_intersection_node(
        self, head1: ListNode, head2: ListNode
    ) -> Optional[ListNode]:
        """
        Returns node where two linked lists intersect using iterative algorithm
        in constant space and linear time.
        :param head1: Head of a linked list
        :param head2: Head of a linked list
        :return: Node where two lists intersect
        """
        if head1 and head2:
            head1, head2 = self.equalize(head1, head2)

            while head1 and head2:
                if head1 is head2:
                    return head1
                else:
                    head1 = head1.next
                    head2 = head2.next
        return None

    @staticmethod
    def get_length(head: ListNode) -> int:
        """
        Return the length of a linked list by traversing it.  Linear time.
        :param head: Head of the linked list
        :return: Length of the list
        """
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def equalize(
        self, head1: ListNode, head2: ListNode
    ) -> Tuple[ListNode, ListNode]:
        """
        Set two linked lists' heads an equal distance from the tail to enable
        comparing lists of differing lengths.
        :param head1: Head of first linked list
        :param head2: Head of second linked list
        :return: Tuple of new heads
        """
        length1 = self.get_length(head1)
        length2 = self.get_length(head2)

        difference = abs(length1 - length2)

        if length1 > length2:
            for _ in range(difference):
                head1 = head1.next

        if length2 > length1:
            for _ in range(difference):
                head2 = head2.next

        return head1, head2
