class Solution:
    def isPalindrome(self, head):
        """Checks if a linked list is a palindrome
        in O(1) space and O(n) time."""
        revnode1 = slow_node = fast_node = head
        revnode2 = revnode1.next

        if head.next is None:
            return True

        while fast_node and fast_node.next:
            fast_node = fast_node.next.next
            slow_node = slow_node.next
            head.next = None
            if revnode1 == slow_node or revnode2 == slow_node:
                continue
            revnode3 = revnode2.next
            revnode2.next = revnode1
            revnode1 = revnode2
            revnode2 = revnode3

        list_is_even = fast_node is None

        list1_head = revnode1
        if list_is_even:
            list2_head = slow_node
        else:
            list2_head = slow_node.next

        while True:
            if list1_head is list2_head:
                return True
            if list1_head.val == list2_head.val:
                list1_head = list1_head.next
                list2_head = list2_head.next
            else:
                return False
