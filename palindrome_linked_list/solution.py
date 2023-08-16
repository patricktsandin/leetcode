class Solution:
    """Checks if a linked list is a palindrome."""
    def isPalindrome(self, head) -> bool:
        current_node = head
        unlinked_list = []
        while current_node:
            unlinked_list.append(current_node.val)
            current_node = current_node.next
        return True if unlinked_list == unlinked_list[::-1] else False
