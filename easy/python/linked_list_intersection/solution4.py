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
        in constant space and linear (O(m+n)) time.

        Visual proof with intersection:
        list 1: A, B, C, D, E, ∅
        list 2: H, I, J, K, L, M, D, E, ∅
        A, B, C, D, E, ∅, H, I, J, K, L, M, D, E, ∅
        H, I, J, K, L, M, D, E, ∅, A, B, C, D, E, ∅
                                            ^

        Visual proof without intersection:
        list 1: A, B, C, D, E, ∅
        list 2: H, I, J, K, L, M, ∅
        A, B, C, D, E, ∅, H, I, J, K, L, M, ∅
        H, I, J, K, L, M, ∅, A, B, C, D, E, ∅
                                            ^

        :param head1: Head of a linked list
        :param head2: Head of a linked list
        :return: Node where two lists intersect
        """
        pointer1 = head1
        pointer2 = head2
        while pointer1 is not pointer2:
            if pointer1:
                pointer1 = pointer1.next
            else:
                pointer1 = head2
            if pointer2:
                pointer2 = pointer2.next
            else:
                pointer2 = head1
        return pointer1
