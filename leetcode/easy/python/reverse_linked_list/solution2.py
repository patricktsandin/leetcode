from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a linked list recursively in linear time and space.
        :param head: Head of a linked list
        :return: Head of reversed linked list
        """
        if head and head.next:
            # Depth-first: keep going until we hit the bottom
            new_head = self.reverse_list(head.next)
            # head.next is the tail of the new list, so we add to it
            head.next.next = head
            # Break the loop we just created
            head.next = None
            return new_head
        else:
            # Bubble up the head after hitting the end
            return head
