class Solution:
    """Remove duplicates from sorted linked list in O(n) time and O(1)
    space, returning a sorted linked list."""
    def deleteDuplicates(self, head):
        pointer = head
        while pointer and pointer.next:
            if pointer.val == pointer.next.val:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next
        return head
