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
        Iterative algorithm in linear time and constant space.
        :param head: Head of linked list possibly containing 'val'
        :param val: Value of nodes to remove
        :return: Head of linked list without nodes of value 'val'
        """
        pointer = head
        while pointer:
            if pointer is head and pointer.val == val:
                head = head.next
                pointer.next, pointer = None, pointer.next
            elif pointer.next and pointer.next.val == val:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next
        return head
